from aiohttp.http import HttpProcessingError

from pyspotify.models import ErrorResponseModel


class PySpotifyException(Exception):
    """Base exception for all custom exceptions raised in the PySpotify package."""

    pass


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
