from aiohttp.http import HttpProcessingError

from pyspotify.models import ErrorResponseModel
from pyspotify.types._spotify_types import AuthScope


class PySpotifyException(Exception):
    """Base exception for all custom exceptions raised in the PySpotify package."""

    pass


class PySpotifyInsufficientScopeError(PySpotifyException):
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


class PySpotifyResponseError(HttpProcessingError, PySpotifyException):
    """Exception raised for unsuccessful Spotify API responses (non-2xx status codes).

    This is the base class for specific error conditions. The error details are extracted
    from the Spotify API error response payload.
    """

    def __init__(self, error_response: ErrorResponseModel) -> None:
        """Initialize the response error exception.

        Args:
            error_response: ErrorResponseModel containing the HTTP status code and error message from the API.
        """
        super(PySpotifyResponseError, self).__init__(code=error_response.status, message=error_response.message)


class PySpotifyUnauthorizedError(PySpotifyResponseError):
    """Exception raised when authentication fails (HTTP 401 Unauthorized).

    This occurs when the access token is invalid, expired, or has insufficient scopes.
    The token should be refreshed by calling authorize() on the auth manager or
    enabling allow_lazy_refresh if using RefreshableAuthManager.
    """

    pass


class PySpotifyTooManyRequests(PySpotifyResponseError):
    """Exception raised when rate limiting is applied (HTTP 429 Too Many Requests).

    This indicates the client has made too many requests in a short time window.
    The PySpotifyClient with max_attempts > 1 will automatically retry with exponential
    backoff when this error is encountered.
    """

    pass
