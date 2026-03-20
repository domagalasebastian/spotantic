from http import HTTPMethod
from http import HTTPStatus
from unittest import mock

import pytest
from aiohttp.client import ClientResponse
from pydantic import SecretStr

from spotantic.client._client import SpotanticClient
from spotantic.client._client import retry_on_failure_decorator
from spotantic.models import ErrorResponseModel
from spotantic.models import RequestModel
from spotantic.models.auth import AccessTokenInfo
from spotantic.models.auth import AuthSettings
from spotantic.types import AuthScope
from spotantic.types.exceptions import SpotanticInsufficientScopeError
from spotantic.types.exceptions import SpotanticInvalidResponseError
from spotantic.types.exceptions import SpotanticResponseError
from spotantic.types.exceptions import SpotanticTooManyRequests
from spotantic.types.exceptions import SpotanticUnauthorizedError


@pytest.fixture
def auth_manager():
    """Fixture for a mock AuthManagerBase."""
    return mock.AsyncMock()


@pytest.fixture
def auth_settings() -> AuthSettings:
    """Fixture for AuthSettings."""
    return AuthSettings(
        client_id=SecretStr("client_id"),
        client_secret=SecretStr("secret"),
    )


@pytest.fixture
def valid_access_token_info() -> AccessTokenInfo:
    """Fixture for a valid AccessTokenInfo."""
    return AccessTokenInfo(
        access_token=SecretStr("access_token"),
        token_type="Bearer",
        expires_in=3600,
        refresh_token=SecretStr("refresh_token"),
        scope="user-read-private user-read-email",
    )


@pytest.fixture
def request_model() -> RequestModel:
    """Fixture for a RequestModel."""
    request = mock.MagicMock(spec=RequestModel)
    request.required_scopes = {AuthScope("user-read-private")}
    request.method_type = HTTPMethod.GET
    request.url = "https://api.spotify.com/v1/me"
    request.headers = mock.MagicMock()
    request.headers.model_dump.return_value = {}
    request.params = None
    request.body = None
    return request


class TestSpotanticClientInit:
    """Tests for SpotanticClient initialization."""

    def test_init_with_valid_max_attempts(self, auth_manager):
        """Test initialization with valid max_attempts."""
        client = SpotanticClient(auth_manager=auth_manager, max_attempts=3)

        assert client.max_attempts == 3

    def test_init_with_default_max_attempts(self, auth_manager):
        """Test initialization with default max_attempts."""
        client = SpotanticClient(auth_manager=auth_manager)

        assert client.max_attempts == 1

    def test_init_with_check_insufficient_scope_true(self, auth_manager):
        """Test initialization with check_insufficient_scope=True."""
        client = SpotanticClient(auth_manager=auth_manager, check_insufficient_scope=True)

        assert client is not None

    def test_init_with_zero_max_attempts_raises_error(self, auth_manager):
        """Test that initialization with max_attempts=0 raises ValueError."""
        with pytest.raises(ValueError, match="max_attempts must be >= 1"):
            SpotanticClient(auth_manager=auth_manager, max_attempts=0)


class TestSpotanticClientMaxAttemptsProperty:
    """Tests for SpotanticClient.max_attempts property."""

    def test_max_attempts_getter(self, auth_manager):
        """Test max_attempts property getter."""
        client = SpotanticClient(auth_manager=auth_manager, max_attempts=5)

        assert client.max_attempts == 5

    def test_max_attempts_setter_with_valid_value(self, auth_manager):
        """Test max_attempts property setter with valid value."""
        client = SpotanticClient(auth_manager=auth_manager, max_attempts=1)

        client.max_attempts = 3

        assert client.max_attempts == 3

    def test_max_attempts_setter_with_zero_raises_error(self, auth_manager):
        """Test that setting max_attempts=0 raises ValueError."""
        client = SpotanticClient(auth_manager=auth_manager)

        with pytest.raises(ValueError, match="max_attempts must be >= 1"):
            client.max_attempts = 0


class TestSpotanticClientGetMissingScopes:
    """Tests for SpotanticClient.__get_missing_scopes static method."""

    def test_get_missing_scopes_no_required_scopes(self, request_model, valid_access_token_info):
        """Test __get_missing_scopes when request has no required scopes."""
        request_model.required_scopes = set()

        missing = SpotanticClient._SpotanticClient__get_missing_scopes(  # type: ignore[attr-defined]
            request_model, valid_access_token_info
        )

        assert missing == set()

    def test_get_missing_scopes_all_scopes_granted(self, request_model, valid_access_token_info):
        """Test __get_missing_scopes when all required scopes are granted."""
        request_model.required_scopes = {AuthScope("user-read-private"), AuthScope("user-read-email")}

        missing = SpotanticClient._SpotanticClient__get_missing_scopes(  # type: ignore[attr-defined]
            request_model, valid_access_token_info
        )

        assert missing == set()

    def test_get_missing_scopes_some_scopes_missing(self, request_model, valid_access_token_info):
        """Test __get_missing_scopes when some required scopes are missing."""
        request_model.required_scopes = {
            AuthScope("user-read-private"),
            AuthScope("user-modify-playback-state"),
        }

        missing = SpotanticClient._SpotanticClient__get_missing_scopes(  # type: ignore[attr-defined]
            request_model, valid_access_token_info
        )

        assert missing == {AuthScope("user-modify-playback-state")}

    def test_get_missing_scopes_all_scopes_missing(self, request_model, valid_access_token_info):
        """Test __get_missing_scopes when no required scopes are granted."""
        request_model.required_scopes = {
            AuthScope("playlist-modify-public"),
            AuthScope("playlist-modify-private"),
        }

        missing = SpotanticClient._SpotanticClient__get_missing_scopes(  # type: ignore[attr-defined]
            request_model, valid_access_token_info
        )

        assert missing == {
            AuthScope("playlist-modify-public"),
            AuthScope("playlist-modify-private"),
        }

    def test_get_missing_scopes_with_none_scope(self, request_model):
        """Test __get_missing_scopes when access token has no scope."""
        access_token_info = AccessTokenInfo(
            access_token=SecretStr("access_token"),
            token_type="Bearer",
            expires_in=3600,
            refresh_token=SecretStr("refresh_token"),
            scope=None,
        )
        request_model.required_scopes = {AuthScope("user-read-private")}

        missing = SpotanticClient._SpotanticClient__get_missing_scopes(  # type: ignore[attr-defined]
            request_model, access_token_info
        )

        assert missing == {AuthScope("user-read-private")}


class TestSpotanticClientRequest:
    """Tests for SpotanticClient.request method."""

    @pytest.mark.asyncio
    async def test_request_checks_insufficient_scope(self, auth_manager, request_model):
        """Test that request checks for insufficient scopes."""
        # Create token with different scope
        access_token_with_limited_scope = AccessTokenInfo(
            access_token=SecretStr("access_token"),
            token_type="Bearer",
            expires_in=3600,
            refresh_token=SecretStr("refresh_token"),
            scope="user-read-private",  # Only this scope
        )
        auth_manager.get_valid_access_token.return_value = access_token_with_limited_scope

        # Request requires a different scope
        request_model.required_scopes = {AuthScope("playlist-modify-public")}

        client = SpotanticClient(auth_manager=auth_manager, check_insufficient_scope=True, max_attempts=1)

        with pytest.raises(
            SpotanticInsufficientScopeError,
            match="Missing scopes",
        ):
            await client.request(request_model)

    @pytest.mark.asyncio
    async def test_request_gets_valid_access_token(self, auth_manager, request_model, valid_access_token_info):
        """Test that request calls get_valid_access_token from auth manager."""
        auth_manager.get_valid_access_token.return_value = valid_access_token_info

        client = SpotanticClient(auth_manager=auth_manager, max_attempts=2)

        # We'll test that it attempts to get a token by verifying auth_manager was called
        with mock.patch("spotantic.client._client.ClientSession") as mock_session_class:
            mock_response = mock.AsyncMock()
            mock_response.ok = True
            mock_response.read = mock.AsyncMock(return_value=b"")

            # Create async context manager for the response
            mock_response_cm = mock.MagicMock()
            mock_response_cm.__aenter__ = mock.AsyncMock(return_value=mock_response)
            mock_response_cm.__aexit__ = mock.AsyncMock(return_value=None)

            # Create session mock with proper request method
            mock_session = mock.AsyncMock()
            mock_session.__aenter__.return_value = mock_session
            mock_session.__aexit__.return_value = None
            mock_session.request = mock.Mock(return_value=mock_response_cm)

            mock_session_class.return_value = mock_session

            try:
                await client.request(request_model)
            except Exception:
                pass

            auth_manager.get_valid_access_token.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_request_skips_scope_check_when_disabled(self, auth_manager, request_model):
        """Test that request skips scope check when check_insufficient_scope=False."""
        # Create token with different scope
        access_token_with_limited_scope = AccessTokenInfo(
            access_token=SecretStr("access_token"),
            token_type="Bearer",
            expires_in=3600,
            refresh_token=SecretStr("refresh_token"),
            scope="user-read-private",
        )
        auth_manager.get_valid_access_token.return_value = access_token_with_limited_scope

        # Request requires a different scope
        request_model.required_scopes = {AuthScope("playlist-modify-public")}

        # With check_insufficient_scope=False, it should not raise
        client = SpotanticClient(auth_manager=auth_manager, check_insufficient_scope=False)

        with mock.patch("spotantic.client._client.ClientSession") as mock_session_class:
            mock_response = mock.AsyncMock()
            mock_response.ok = True
            mock_response.read = mock.AsyncMock(return_value=b"")

            # Create async context manager for the response
            mock_response_cm = mock.MagicMock()
            mock_response_cm.__aenter__ = mock.AsyncMock(return_value=mock_response)
            mock_response_cm.__aexit__ = mock.AsyncMock(return_value=None)

            # Create session mock with proper request method
            mock_session = mock.AsyncMock()
            mock_session.__aenter__.return_value = mock_session
            mock_session.__aexit__.return_value = None
            mock_session.request = mock.Mock(return_value=mock_response_cm)

            mock_session_class.return_value = mock_session

            # Should not raise SpotanticInsufficientScopeError
            result = await client.request(request_model)
            assert result is None


class TestSpotanticClientRequestJson:
    """Tests for SpotanticClient.request_json method."""

    @pytest.mark.asyncio
    async def test_request_json_with_empty_response_raises_error(
        self, auth_manager, request_model, valid_access_token_info
    ):
        """Test that request_json raises error when response is empty."""
        auth_manager.get_valid_access_token.return_value = valid_access_token_info

        client = SpotanticClient(auth_manager=auth_manager)

        # Mock the request method to return None (empty response)
        with mock.patch.object(client, "request", new_callable=mock.AsyncMock, return_value=None):
            with pytest.raises(
                SpotanticInvalidResponseError,
                match="Expected JSON response.*got empty body",
            ):
                await client.request_json(request_model)

    @pytest.mark.asyncio
    async def test_request_json_with_invalid_json_raises_error(
        self, auth_manager, request_model, valid_access_token_info
    ):
        """Test that request_json raises error when response is not valid JSON."""
        auth_manager.get_valid_access_token.return_value = valid_access_token_info

        client = SpotanticClient(auth_manager=auth_manager)

        # Mock the request method to return invalid JSON
        with mock.patch.object(client, "request", new_callable=mock.AsyncMock, return_value=b"invalid json"):
            with pytest.raises(
                SpotanticInvalidResponseError,
                match="Expected JSON response, got invalid JSON",
            ):
                await client.request_json(request_model)


class TestSpotanticClientCheckResponse:
    """Tests for SpotanticClient.__check_response static method."""

    @pytest.mark.asyncio
    async def test_check_response_with_ok_response(self):
        """Test __check_response with successful response."""
        mock_response = mock.AsyncMock(spec=ClientResponse)
        mock_response.ok = True

        # Should not raise any exception
        await SpotanticClient._SpotanticClient__check_response(mock_response)  # type: ignore[attr-defined]

    @pytest.mark.asyncio
    async def test_check_response_with_unauthorized_error(self):
        """Test __check_response raises SpotanticUnauthorizedError for 401."""
        mock_response = mock.AsyncMock(spec=ClientResponse)
        mock_response.ok = False
        mock_response.status = HTTPStatus.UNAUTHORIZED

        error_response_dict = {
            "error": {
                "status": 401,
                "message": "The access token expired",
            }
        }
        mock_response.json = mock.AsyncMock(return_value=error_response_dict)

        # Create a real ErrorResponseModel to avoid mocking Pydantic models
        error_model = ErrorResponseModel(status=HTTPStatus.UNAUTHORIZED, message="The access token expired")

        with mock.patch.object(
            ErrorResponseModel,
            "model_validate",
            return_value=error_model,
        ):
            with pytest.raises(SpotanticUnauthorizedError):
                await SpotanticClient._SpotanticClient__check_response(mock_response)  # type: ignore[attr-defined]

    @pytest.mark.asyncio
    async def test_check_response_with_too_many_requests_error(self):
        """Test __check_response raises SpotanticTooManyRequests for 429."""
        mock_response = mock.AsyncMock(spec=ClientResponse)
        mock_response.ok = False
        mock_response.status = HTTPStatus.TOO_MANY_REQUESTS

        error_response_dict = {
            "error": {
                "status": 429,
                "message": "Rate limit exceeded",
            }
        }
        mock_response.json = mock.AsyncMock(return_value=error_response_dict)

        error_model = ErrorResponseModel(status=HTTPStatus.TOO_MANY_REQUESTS, message="Rate limit exceeded")

        with mock.patch.object(
            ErrorResponseModel,
            "model_validate",
            return_value=error_model,
        ):
            with pytest.raises(SpotanticTooManyRequests):
                await SpotanticClient._SpotanticClient__check_response(mock_response)  # type: ignore[attr-defined]

    @pytest.mark.asyncio
    async def test_check_response_with_generic_error(self):
        """Test __check_response raises SpotanticResponseError for other errors."""
        mock_response = mock.AsyncMock(spec=ClientResponse)
        mock_response.ok = False
        mock_response.status = HTTPStatus.BAD_REQUEST

        error_response_dict = {
            "error": {
                "status": 400,
                "message": "Invalid request",
            }
        }
        mock_response.json = mock.AsyncMock(return_value=error_response_dict)

        error_model = ErrorResponseModel(status=HTTPStatus.BAD_REQUEST, message="Invalid request")

        with mock.patch.object(
            ErrorResponseModel,
            "model_validate",
            return_value=error_model,
        ):
            with pytest.raises(SpotanticResponseError):
                await SpotanticClient._SpotanticClient__check_response(mock_response)  # type: ignore[attr-defined]

    @pytest.mark.asyncio
    async def test_check_response_with_invalid_error_response(self):
        """Test __check_response raises SpotanticInvalidResponseError when cannot parse error."""
        mock_response = mock.AsyncMock(spec=ClientResponse)
        mock_response.ok = False
        mock_response.status = HTTPStatus.BAD_REQUEST
        mock_response.json = mock.AsyncMock(side_effect=ValueError("Invalid JSON"))

        with pytest.raises(
            SpotanticInvalidResponseError,
            match="Invalid error response",
        ):
            await SpotanticClient._SpotanticClient__check_response(mock_response)  # type: ignore[attr-defined]


class TestRetryOnFailureDecorator:
    """Tests for retry_on_failure_decorator."""

    @pytest.mark.asyncio
    async def test_decorator_returns_result_on_success(self, auth_manager):
        """Test decorator returns result on successful call."""

        async def mock_func(client: SpotanticClient, *args, **kwargs):
            return b"success"

        decorated = retry_on_failure_decorator(mock_func)
        client = SpotanticClient(auth_manager=auth_manager, max_attempts=3)

        result = await decorated(client)

        assert result == b"success"

    @pytest.mark.asyncio
    async def test_decorator_retries_on_unauthorized_error(self, auth_manager):
        """Test decorator retries on SpotanticUnauthorizedError."""
        call_count = 0

        async def mock_func(client: SpotanticClient, *args, **kwargs):
            nonlocal call_count
            call_count += 1
            if call_count < 2:
                error_model = ErrorResponseModel(status=HTTPStatus.UNAUTHORIZED, message="Unauthorized")
                raise SpotanticUnauthorizedError(error_response=error_model)
            return b"success"

        decorated = retry_on_failure_decorator(mock_func)
        client = SpotanticClient(auth_manager=auth_manager, max_attempts=3)

        result = await decorated(client)

        assert result == b"success"
        assert call_count == 2

    @pytest.mark.asyncio
    async def test_decorator_retries_on_too_many_requests_error(self, auth_manager):
        """Test decorator retries on SpotanticTooManyRequests."""
        call_count = 0

        async def mock_func(client: SpotanticClient, *args, **kwargs):
            nonlocal call_count
            call_count += 1
            if call_count < 2:
                error_model = ErrorResponseModel(status=HTTPStatus.TOO_MANY_REQUESTS, message="Too many requests")
                raise SpotanticTooManyRequests(error_response=error_model)
            return b"success"

        decorated = retry_on_failure_decorator(mock_func)
        client = SpotanticClient(auth_manager=auth_manager, max_attempts=3)

        result = await decorated(client)

        assert result == b"success"
        assert call_count == 2

    @pytest.mark.asyncio
    async def test_decorator_raises_error_after_max_attempts(self, auth_manager):
        """Test decorator raises error after exhausting max_attempts."""
        call_count = 0

        async def mock_func(client: SpotanticClient, *args, **kwargs):
            nonlocal call_count
            call_count += 1
            error_model = ErrorResponseModel(status=HTTPStatus.UNAUTHORIZED, message="Unauthorized")
            raise SpotanticUnauthorizedError(error_response=error_model)

        decorated = retry_on_failure_decorator(mock_func)
        client = SpotanticClient(auth_manager=auth_manager, max_attempts=2)

        with pytest.raises(SpotanticUnauthorizedError):
            await decorated(client)

        # Verify the function was called max_attempts times
        assert call_count == 2

    @pytest.mark.asyncio
    async def test_decorator_does_not_retry_other_exceptions(self, auth_manager):
        """Test decorator does not retry on exceptions other than 401/429."""
        call_count = 0

        async def mock_func(client: SpotanticClient, *args, **kwargs):
            nonlocal call_count
            call_count += 1
            error_model = ErrorResponseModel(status=HTTPStatus.BAD_REQUEST, message="Bad Request")
            raise SpotanticResponseError(error_response=error_model)

        decorated = retry_on_failure_decorator(mock_func)
        client = SpotanticClient(auth_manager=auth_manager, max_attempts=3)

        with pytest.raises(SpotanticResponseError):
            await decorated(client)

        assert call_count == 1
