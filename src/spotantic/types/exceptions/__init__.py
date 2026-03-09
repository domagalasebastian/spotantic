from ._custom_exceptions import SpotanticAuthAccessTokenRequestError
from ._custom_exceptions import SpotanticAuthCodeRequestError
from ._custom_exceptions import SpotanticAuthorizationError
from ._custom_exceptions import SpotanticAuthSecurityError
from ._custom_exceptions import SpotanticException
from ._custom_exceptions import SpotanticInsufficientScopeError
from ._custom_exceptions import SpotanticInvalidResponseError
from ._custom_exceptions import SpotanticResponseError
from ._custom_exceptions import SpotanticTooManyRequests
from ._custom_exceptions import SpotanticUnauthorizedError

__all__ = [
    "SpotanticAuthAccessTokenRequestError",
    "SpotanticAuthCodeRequestError",
    "SpotanticAuthSecurityError",
    "SpotanticAuthorizationError",
    "SpotanticException",
    "SpotanticInsufficientScopeError",
    "SpotanticInvalidResponseError",
    "SpotanticResponseError",
    "SpotanticTooManyRequests",
    "SpotanticUnauthorizedError",
]
