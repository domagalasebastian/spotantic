from http import HTTPMethod
from typing import Any
from typing import Dict
from typing import Generic
from typing import Optional
from typing import TypeVar

from pydantic import BaseModel
from pydantic import Field
from pydantic import HttpUrl
from pydantic import model_validator
from yarl import URL

ParamsModelT = TypeVar("ParamsModelT")
BodyModelT = TypeVar("BodyModelT")
API_BASE_URL = URL("https://api.spotify.com/v1/")


class RequestModel(BaseModel, Generic[ParamsModelT, BodyModelT]):
    url: Optional[HttpUrl] = None
    endpoint: Optional[str] = Field(None, repr=False)
    method_type: HTTPMethod
    params: Optional[ParamsModelT] = None
    body: Optional[BodyModelT] = None

    @model_validator(mode="before")
    def get_url_from_endpoint(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        url = values.get("url")
        endpoint = values.get("endpoint")

        if url is None and endpoint is None:
            raise ValueError("Either 'url' or 'endpoint' must be provided!")

        if url is None and isinstance(endpoint, str):
            values["url"] = str(API_BASE_URL / endpoint)

        return values
