from __future__ import annotations

from asyncio import sleep
from collections.abc import Awaitable
from collections.abc import Callable
from functools import wraps
from http import HTTPStatus
from typing import Concatenate
from typing import ParamSpec

from aiohttp.client import ClientResponse
from aiohttp.client import ClientSession
from pydantic_core import from_json

from pyspotify._utils.logger import logger
from pyspotify.auth._auth_manager_base import AuthManagerBase
from pyspotify.models import ErrorResponseModel
from pyspotify.models import RequestModel
from pyspotify.models.auth import AccessTokenInfo
from pyspotify.types import APIResponse
from pyspotify.types import AuthScope
from pyspotify.types.exceptions import PySpotifyInsufficientScopeError
from pyspotify.types.exceptions import PySpotifyResponseError
from pyspotify.types.exceptions import PySpotifyTooManyRequests
from pyspotify.types.exceptions import PySpotifyUnauthorizedError

P = ParamSpec("P")


def retry_on_failure_decorator(
    func: Callable[Concatenate[PySpotifyClient, P], Awaitable[APIResponse]],
) -> Callable[Concatenate[PySpotifyClient, P], Awaitable[APIResponse]]:
    """Decorator to retry API requests on authentication or rate-limit failures.

    Implements exponential backoff retry strategy for transient failures (401 Unauthorized
    and 429 Too Many Requests). Other exceptions are not retried.

    Args:
        func: The async function to decorate. Should accept a PySpotifyClient as first argument.

    Returns:
        Wrapped function that retries on specified failure types up to client.max_attempts times.
    """
    delay = 1.0
    backoff = 2.0

    @wraps(func)
    async def wrapper(client: PySpotifyClient, *args: P.args, **kwargs: P.kwargs) -> APIResponse:
        for attempt in range(2, client.max_attempts + 1):
            try:
                return await func(client, *args, **kwargs)
            except (PySpotifyUnauthorizedError, PySpotifyTooManyRequests) as e:
                client._logger.error(f"Attempt {attempt}/{client.max_attempts} failed with {e.__class__.__name__}: {e}")
                if attempt == client.max_attempts:
                    raise

                wait_time = delay * (backoff ** (attempt - 1))
                client._logger.warning(
                    f"Request failed due to {e.__class__.__name__}; retrying in {wait_time:.1f}s (attempt {attempt + 1}/{client.max_attempts})"
                )
                await sleep(wait_time)

    return wrapper


class PySpotifyClient:
    """Client for interacting with the Spotify Web API.

    This client handles HTTP requests to the Spotify API, including authentication,
    scope validation, and automatic retry logic with exponential backoff for
    transient failures (authorization and rate limit errors).
    """

    def __init__(
        self, auth_manager: AuthManagerBase, *, max_attempts: int = 1, check_insufficient_scope: bool = True
    ) -> None:
        """Initialize the PySpotify client.

        Args:
            auth_manager: Authentication manager responsible for OAuth2 flow and token lifecycle management.
            max_attempts: Maximum number of retry attempts for failed requests (default: 1, no retries).
            check_insufficient_scope: Whether to check and raise an error if the access token lacks required scopes
                (default: True).

        Raises:
            ValueError: If max_attempts is less than 1.
        """
        if max_attempts < 1:
            raise ValueError(f"max_attempts must be >= 1, got {max_attempts}")

        self._logger = logger.getChild("client")
        self.__auth_manager = auth_manager
        self.__max_attempts = max_attempts
        self.__check_insufficient_scope = check_insufficient_scope

    @property
    def max_attempts(self) -> int:
        return self.__max_attempts

    @max_attempts.setter
    def max_attempts(self, value: int) -> None:
        """Set the maximum number of retry attempts.

        Args:
            value: Number of attempts (must be >= 1).

        Raises:
            ValueError: If value is less than 1.
        """
        if value < 1:
            raise ValueError(f"max_attempts must be >= 1, got {value}")

        self.__max_attempts = value

    @staticmethod
    def __get_missing_scopes(request: RequestModel, access_token_info: AccessTokenInfo) -> set[AuthScope]:
        """Determine which required scopes are missing from the access token.

        Args:
            request: The request model containing required scopes.
            access_token_info: The current access token info with granted scopes.

        Returns:
            Set of scopes required by the request but not present in the access token.
        """
        required_scopes = request.required_scopes
        if access_token_info.scope is None:
            return required_scopes

        client_scopes = {AuthScope(scope) for scope in access_token_info.scope.split(" ")}

        return required_scopes - client_scopes

    @retry_on_failure_decorator
    async def request(self, request: RequestModel) -> APIResponse:
        """Execute an HTTP request described by `request` and return parsed response.

        Args:
            request: `RequestModel` describing method, url, headers, params and body.

        Returns:
            Parsed API response or `None` for empty or unparsable responses.
        """
        self._logger.debug(f"Request: {request}")
        access_token_info = await self.__auth_manager.get_valid_access_token()

        if self.__check_insufficient_scope:
            if missing_scopes := self.__get_missing_scopes(request, access_token_info):
                raise PySpotifyInsufficientScopeError(missing_scopes=missing_scopes)

        auth_header = access_token_info.get_authorization_header()

        method = request.method_type
        url = str(request.url)
        headers = request.headers.model_dump(mode="json", exclude_none=True) | auth_header
        params = request.params.model_dump(mode="json", exclude_none=True) if request.params is not None else None
        data = request.body.model_dump_json(exclude_none=True) if request.body is not None else None

        async with ClientSession() as session:
            async with session.request(
                method=method,
                headers=headers,
                url=url,
                params=params,
                data=data,
                raise_for_status=self.__check_response,
            ) as resp:
                response_data = await resp.read()
                response_data = response_data.strip()

        if not response_data:
            return None

        try:
            json_data = from_json(response_data)
        except ValueError:
            self._logger.debug(f"Response body (raw): {response_data}")
            self._logger.warning("Failed to deserialize response body as JSON; returning None.")
            return None
        else:
            return json_data

    @staticmethod
    async def __check_response(response: ClientResponse) -> None:
        """Raise appropriate exception in case of error response.

        Args:
            response: A response from the server.

        Raises:
            PySpotifyUnauthorizedError: In case of bad or expired token.
            PySpotifyTooManyRequests: In case of rate limiting has been applied.
            PySpotifyResponseError: Any other unsuccessful response.
        """
        if response.ok:
            return

        status = HTTPStatus(response.status)
        payload = await response.json()
        err_info = ErrorResponseModel(**payload.get("error"))
        if status == HTTPStatus.UNAUTHORIZED:
            raise PySpotifyUnauthorizedError(error_response=err_info)
        elif status == HTTPStatus.TOO_MANY_REQUESTS:
            raise PySpotifyTooManyRequests(error_response=err_info)
        else:
            raise PySpotifyResponseError(error_response=err_info)
