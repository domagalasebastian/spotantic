from pydantic import BaseModel


class APICallModel[RequestModelT, ResponseModelT, DataModelT](BaseModel):
    request: RequestModelT
    response: ResponseModelT
    data: DataModelT
