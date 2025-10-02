from http import HTTPMethod
from typing import Any
from typing import Dict
from typing import Optional
from typing import Set

from aiohttp.hdrs import CONTENT_ENCODING
from aiohttp.hdrs import CONTENT_LANGUAGE
from aiohttp.hdrs import CONTENT_LENGTH
from aiohttp.hdrs import CONTENT_TYPE
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl
from pydantic import model_validator
from yarl import URL

from pyspotify.custom_types import Scope

API_BASE_URL = URL("https://api.spotify.com/v1/")


class EntityHeadersModel(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)
    content_type: Optional[str] = Field(default=None, serialization_alias=CONTENT_TYPE)
    content_length: Optional[int] = Field(default=None, serialization_alias=CONTENT_LENGTH)
    content_encoding: Optional[str] = Field(default=None, serialization_alias=CONTENT_ENCODING)
    content_language: Optional[str] = Field(default=None, serialization_alias=CONTENT_LANGUAGE)


class RequestHeadersModel(EntityHeadersModel):
    pass


class RequestModel[ParamsModelT, BodyModelT](BaseModel):
    required_scopes: Set[Scope] = set()
    url: Optional[HttpUrl] = None
    endpoint: Optional[str] = None
    method_type: HTTPMethod
    headers: RequestHeadersModel = RequestHeadersModel()
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
