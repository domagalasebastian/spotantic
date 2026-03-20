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

from spotantic._utils.logger import logger
from spotantic.auth._auth_manager_base import AuthManagerBase
from spotantic.models import ErrorResponseModel
from spotantic.models import RequestModel
from spotantic.models.auth import AccessTokenInfo
from spotantic.types import AuthScope
from spotantic.types import JsonAPIResponse
from spotantic.types import RawAPIResponse
from spotantic.types.exceptions import SpotanticInsufficientScopeError
from spotantic.types.exceptions import SpotanticInvalidResponseError
from spotantic.types.exceptions import SpotanticResponseError
from spotantic.types.exceptions import SpotanticTooManyRequests
from spotantic.types.exceptions import SpotanticUnauthorizedError

P = ParamSpec("P")


def retry_on_failure_decorator(
    func: Callable[Concatenate[SpotanticClient, P], Awaitable[RawAPIResponse]],
) -> Callable[Concatenate[SpotanticClient, P], Awaitable[RawAPIResponse]]:
    """Decorator to retry API requests on authentication or rate-limit failures.

    Implements exponential backoff retry strategy for transient failures (401 Unauthorized
    and 429 Too Many Requests). Other exceptions are not retried.

    Args:
        func: The async function to decorate. Should accept a SpotanticClient as first argument.

    Returns:
        Wrapped function that retries on specified failure types up to client.max_attempts times.
    """
    delay = 1.0
    backoff = 2.0

    @wraps(func)
    async def wrapper(client: SpotanticClient, *args: P.args, **kwargs: P.kwargs) -> RawAPIResponse:
        for attempt in range(1, client.max_attempts + 1):
            try:
                return await func(client, *args, **kwargs)
            except (SpotanticUnauthorizedError, SpotanticTooManyRequests) as e:
                client._logger.error(f"Attempt {attempt}/{client.max_attempts} failed with {e.__class__.__name__}: {e}")
                if attempt == client.max_attempts:
                    raise

                wait_time = delay * (backoff ** (attempt - 1))
                client._logger.warning(
                    f"Request failed due to {e.__class__.__name__}; retrying in {wait_time:.1f}s (attempt {attempt + 1}/{client.max_attempts})"
                )
                await sleep(wait_time)

    return wrapper


class SpotanticClient:
    """Client for interacting with the Spotify Web API.

    This client handles HTTP requests to the Spotify API, including authentication,
    scope validation, and automatic retry logic with exponential backoff for
    transient failures (authorization and rate limit errors).
    """

    def __init__(
        self, auth_manager: AuthManagerBase, *, max_attempts: int = 1, check_insufficient_scope: bool = True
    ) -> None:
        """Initialize the Spotantic client.

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
    async def request(self, request: RequestModel) -> RawAPIResponse:
        """Execute an HTTP request described by ``request`` and return raw response.

        Args:
            request: `RequestModel` describing method, url, headers, params and body.

        Returns:
            Raw API response or `None` for empty responses.
        """
        self._logger.debug(f"Request: {request}")
        access_token_info = await self.__auth_manager.get_valid_access_token()

        if self.__check_insufficient_scope:
            if missing_scopes := self.__get_missing_scopes(request, access_token_info):
                raise SpotanticInsufficientScopeError(missing_scopes=missing_scopes)

        auth_header = access_token_info.get_authorization_header()

        async with ClientSession() as session:
            async with session.request(
                **request._to_http_request_kwargs(auth_headers=auth_header),
                raise_for_status=self.__check_response,
            ) as resp:
                response_data = await resp.read()
                response_data = response_data.strip()

        return response_data if response_data else None

    async def request_json(self, request: RequestModel) -> JsonAPIResponse:
        """Execute an HTTP request described by ``request`` and return parsed response.

        Args:
            request: `RequestModel` describing method, url, headers, params and body.

        Returns:
            Parsed API response as Python object.

        Raises:
            SpotanticInvalidResponseError: If server response is empty or cannot be deserialized.
        """
        response_data = await self.request(request=request)
        if response_data is None:
            raise SpotanticInvalidResponseError(f"Expected JSON response from {request.url}, got empty body.")

        try:
            json_data = from_json(response_data)
        except ValueError as e:
            raise SpotanticInvalidResponseError("Expected JSON response, got invalid JSON.") from e

        return json_data

    @staticmethod
    async def __check_response(response: ClientResponse) -> None:
        """Raise appropriate exception in case of error response.

        Args:
            response: A response from the server.

        Raises:
            SpotanticUnauthorizedError: In case of bad or expired token.
            SpotanticTooManyRequests: In case of rate limiting has been applied.
            SpotanticResponseError: Any other unsuccessful response.
            SpotanticInvalidResponseError: Request failed and response does not match Spotify error response type.
        """
        if response.ok:
            return

        status = HTTPStatus(response.status)
        try:
            payload = await response.json()
        except Exception as e:
            raise SpotanticInvalidResponseError(
                "Invalid error response! Expected to get response with the error details!"
            ) from e

        err_info = ErrorResponseModel.model_validate(payload.get("error"))
        if status == HTTPStatus.UNAUTHORIZED:
            raise SpotanticUnauthorizedError(error_response=err_info)
        elif status == HTTPStatus.TOO_MANY_REQUESTS:
            raise SpotanticTooManyRequests(error_response=err_info)
        else:
            raise SpotanticResponseError(error_response=err_info)
