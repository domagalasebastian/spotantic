from aiohttp.http import HttpProcessingError

from spotantic.models import ErrorResponseModel
from spotantic.types._spotify_types import AuthScope


class SpotanticException(Exception):
    """Base exception for all custom exceptions raised in the Spotantic package."""

    pass


class SpotanticAuthorizationError(SpotanticException):
    """Base exception for authorization-related errors in the OAuth2 flow.

    This is the parent class for all authentication and authorization failures
    including security violations, code request failures, and token request failures.
    """

    pass


class SpotanticAuthSecurityError(SpotanticAuthorizationError):
    """Exception raised when a security check fails during the OAuth2 authorization flow.

    This typically occurs when the state parameter in the OAuth2 callback doesn't match
    the expected state, indicating a potential CSRF (Cross-Site Request Forgery) attack.
    """

    pass


class SpotanticAuthCodeRequestError(SpotanticAuthorizationError):
    """Exception raised when the OAuth2 authorization code request fails.

    This occurs when Spotify's authorization endpoint returns an error parameter
    instead of an authorization code, typically due to user denial or invalid request parameters.
    """

    pass


class SpotanticAuthAccessTokenRequestError(SpotanticAuthorizationError):
    """Exception raised when the OAuth2 access token request fails.

    This occurs when the token endpoint returns a non-200 status code, typically due to
    invalid authorization code, invalid client credentials, or other token request issues.
    """

    pass


class SpotanticInsufficientScopeError(SpotanticException):
    """Exception raised when the access token lacks required scopes for a request.

    This exception is raised when scope validation is enabled on the client and
    a request requires scopes that are not granted in the current access token.
    """

    def __init__(self, missing_scopes: set[AuthScope]) -> None:
        """Initialize the insufficient scope error.

        Args:
            missing_scopes: Set of scopes that are required but not available.
        """
        self.missing_scopes = missing_scopes

    def __str__(self) -> str:
        """Return a human-readable string representation of the missing scopes.

        Returns:
            String in format "Missing scopes: scope1,scope2,..."
        """
        return f"Missing scopes: {','.join(self.missing_scopes)}"

    def __repr__(self) -> str:
        """Return a developer-friendly representation of the exception.

        Returns:
            String representation with class name and missing scopes.
        """
        return f"<{self.__class__.__name__}: Missing scopes={self.missing_scopes!r}>"


class SpotanticResponseError(HttpProcessingError, SpotanticException):
    """Exception raised for unsuccessful Spotify API responses (non-2xx status codes).

    This is the base class for specific error conditions. The error details are extracted
    from the Spotify API error response payload.
    """

    def __init__(self, error_response: ErrorResponseModel) -> None:
        """Initialize the response error exception.

        Args:
            error_response: ErrorResponseModel containing the HTTP status code and error message from the API.
        """
        super(SpotanticResponseError, self).__init__(code=error_response.status, message=error_response.message)


class SpotanticUnauthorizedError(SpotanticResponseError):
    """Exception raised when authentication fails (HTTP 401 Unauthorized).

    This occurs when the access token is invalid, expired, or has insufficient scopes.
    The token should be refreshed by calling authorize() on the auth manager or
    enabling allow_lazy_refresh if using RefreshableAuthManager.
    """

    pass


class SpotanticTooManyRequests(SpotanticResponseError):
    """Exception raised when rate limiting is applied (HTTP 429 Too Many Requests).

    This indicates the client has made too many requests in a short time window.
    The SpotanticClient with max_attempts > 1 will automatically retry with exponential
    backoff when this error is encountered.
    """

    pass
