from __future__ import annotations

from http import HTTPMethod
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

    @model_validator(mode="after")
    def get_url_from_endpoint(self) -> RequestModel:
        if self.url is not None:
            return self

        if self.endpoint is None:
            raise ValueError("Either 'url' or 'endpoint' must be provided!")

        self.url = HttpUrl(str(API_BASE_URL / self.endpoint))

        return self
