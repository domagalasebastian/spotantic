from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from http import HTTPMethod
from typing import Optional
from typing import Union

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

from spotantic._utils.models._aiohttp_request_kwargs_typed_dict import AiohttpRequestKwargs
from spotantic.types import AuthScope

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
    """Model representing HTTP request headers.

    Inherits common entity headers and can be extended with additional request-specific headers.
    """

    pass


class RequestBodyModel(BaseModel, ABC):
    """Abstract base model for request bodies.

    Specific request body models should inherit from this class and implement
    necessary validation and serialization logic.
    """

    @abstractmethod
    def to_http_body(self) -> Optional[Union[str, bytes]]:
        """Convert the model to a format suitable for the HTTP request body.

        Returns:
            The serialized request body data, or `None` if there is no body.
        """
        pass


class RequestBodyJsonModel(RequestBodyModel):
    """Base model for request bodies that should be serialized to JSON."""

    def to_http_body(self) -> Optional[str]:
        """Serialize the model to a JSON string for the HTTP request body.

        Returns:
            The serialized JSON string, or `None` if there is no body.
        """
        return self.model_dump_json(exclude_none=True)


class RequestModel[ParamsModelT: (BaseModel, None), BodyModelT: (RequestBodyModel, None)](BaseModel):
    """Model representing a complete Spotify API request.

    Encapsulates all information needed to make an HTTP request to the Spotify API:
    the endpoint URL, HTTP method, headers, query parameters, and request body.
    """

    required_scopes: set[AuthScope] = Field(default_factory=set)
    """Required authorization scopes for the request."""

    url: Optional[HttpUrl] = None
    """Request URL. If specified, the `endpoint` value is ignored."""

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
        """Populate `url` from `endpoint` if not explicitly provided.

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
                raise ValueError(f"URL must start with Spotify API base URL ({API_BASE_URL}); got {self.url}")

            return self

        if self.endpoint is None:
            raise ValueError(
                "Either 'url' or 'endpoint' must be provided. Use 'endpoint' for standard Spotify API calls "
                "or 'url' for custom URLs (must start with API base URL)."
            )

        self.url = HttpUrl(str(API_BASE_URL / self.endpoint))

        return self

    def _to_http_request_kwargs(self, auth_headers: dict[str, str]) -> AiohttpRequestKwargs:
        """Convert the model to a dictionary of data suitable for making an HTTP request.

        This method prepares the data for the HTTP request by converting the URL, headers,
        query parameters, and body into the appropriate formats. It also allows for optional
        overrides of any of these components.

        Args:
            auth_headers: A dictionary containing the authorization headers for the request.

        Returns:
            A dictionary containing the URL, method, headers, params, and data for the HTTP request.
        """
        data = AiohttpRequestKwargs(
            url=str(self.url),
            method=self.method_type.value,
            headers=self.headers.model_dump(mode="json", exclude_none=True) | auth_headers,
            params=self.params.model_dump(mode="json", exclude_none=True) if self.params is not None else None,
            data=self.body.to_http_body() if self.body is not None else None,
        )

        return data
