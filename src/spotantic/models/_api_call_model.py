from typing import Generic
from typing import TypeVar

from pydantic import BaseModel
from pydantic import ConfigDict

from spotantic.types import APIResponse

RequestModelT = TypeVar("RequestModelT")
ResponseT = TypeVar("ResponseT", bound=APIResponse)
DataModelT_co = TypeVar("DataModelT_co", covariant=True)


class APICallModel(BaseModel, Generic[RequestModelT, ResponseT, DataModelT_co]):
    """Generic container model representing an API call."""

    model_config = ConfigDict(frozen=True)

    request: RequestModelT
    """Represents the request."""

    response: ResponseT
    """Represents the response."""

    data: DataModelT_co
    """Represents associated or derived data."""
