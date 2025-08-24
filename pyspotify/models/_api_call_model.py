from typing import Generic
from typing import TypeVar

from pydantic import BaseModel

RequestModelT = TypeVar("RequestModelT")
ResponseModelT = TypeVar("ResponseModelT")
DataModelT = TypeVar("DataModelT")


class APICallModel(BaseModel, Generic[RequestModelT, ResponseModelT, DataModelT]):
    request: RequestModelT
    response: ResponseModelT
    data: DataModelT
