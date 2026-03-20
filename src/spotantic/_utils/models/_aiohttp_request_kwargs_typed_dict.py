from typing import Any
from typing import Optional
from typing import TypedDict
from typing import Union


class AiohttpRequestKwargs(TypedDict):
    """TypedDict representing the keyword arguments for an aiohttp request."""

    method: str
    """HTTP method for the request (e.g., 'GET', 'POST')."""

    url: str
    """URL for the request."""

    headers: dict[str, str]
    """Headers for the request."""

    params: Optional[dict[str, Any]]
    """Query parameters for the request."""

    data: Optional[Union[str, bytes]]
    """Data for the request body."""
