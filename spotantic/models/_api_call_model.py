from pydantic import BaseModel


class APICallModel[RequestModelT, ResponseModelT, DataModelT](BaseModel):
    """Generic container model representing an API call."""

    request: RequestModelT
    """Pydantic model or type representing the request."""

    response: ResponseModelT
    """Pydantic model or type representing the response."""

    data: DataModelT
    """Pydantic model or type representing associated or derived data."""
