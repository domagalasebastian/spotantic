from __future__ import annotations

from http import HTTPMethod
from typing import Optional

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
    """Model representing common HTTP entity headers."""

    model_config = ConfigDict(serialize_by_alias=True)

    content_type: Optional[str] = Field(default=None, serialization_alias=CONTENT_TYPE)
    """Media type of the entity body (e.g., `application/json`)."""

    content_length: Optional[int] = Field(default=None, serialization_alias=CONTENT_LENGTH)
    """Size of the entity body in bytes."""

    content_encoding: Optional[str] = Field(default=None, serialization_alias=CONTENT_ENCODING)
    """Encoding transformations applied to the entity body (e.g., `gzip`)."""

    content_language: Optional[str] = Field(default=None, serialization_alias=CONTENT_LANGUAGE)
    """Natural language(s) of the intended audience for the entity body (e.g., `en`)."""


class RequestHeadersModel(EntityHeadersModel):
    """Model representing HTTP headers."""

    pass


class RequestModel[ParamsModelT, BodyModelT](BaseModel):
    """Model representing the API request."""

    required_scopes: set[Scope] = Field(default_factory=set)
    """Required authorization scopes for the request."""

    url: Optional[HttpUrl] = None
    """Request URL. If specfied, the `endpoint` value is ignored."""

    endpoint: Optional[str] = None
    """Endpoint associated with the request."""

    method_type: HTTPMethod
    """HTTP method for the request."""

    headers: RequestHeadersModel = Field(default_factory=RequestHeadersModel)
    """Headers for the request."""

    params: Optional[ParamsModelT] = None
    """Params model for the request."""

    body: Optional[BodyModelT] = None
    """Body model for the request."""

    @model_validator(mode="after")
    def get_url_from_endpoint(self) -> RequestModel:
        """
        Populate `url` from `endpoint` if not explicitly provided.

        This validator runs after model initialization. If `url` is already set,
        it is left unchanged. Otherwise, the URL is constructed by joining the
        configured API base URL with the provided endpoint.

        Returns:
            The validated model instance with `url` populated.

        Raises:
            ValueError: If neither `url` nor `endpoint` is provided.
        """
        if self.url is not None:
            if not str(self.url).startswith(str(API_BASE_URL)):
                raise ValueError(f"`url` must start with API base URL: {API_BASE_URL}")

            return self

        if self.endpoint is None:
            raise ValueError("Either 'url' or 'endpoint' must be provided!")

        self.url = HttpUrl(str(API_BASE_URL / self.endpoint))

        return self
