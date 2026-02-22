from pydantic import BaseModel

from spotantic.types import APIResponse


class APICallModel[RequestModelT, ResponseT: APIResponse, DataModelT](BaseModel):
    """Generic container model representing an API call."""

    request: RequestModelT
    """Represents the request."""

    response: ResponseT
    """Represents the response."""

    data: DataModelT
    """Represents associated or derived data."""
