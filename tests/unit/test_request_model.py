from http import HTTPMethod

import pytest
from pydantic import BaseModel
from pydantic import HttpUrl
from pydantic import ValidationError

from spotantic.models import EntityHeadersModel
from spotantic.models import RequestBodyJsonModel
from spotantic.models import RequestHeadersModel
from spotantic.models import RequestModel
from spotantic.models._request_model import API_BASE_URL
from spotantic.types import AuthScope


class TestEntityHeadersModel:
    """Tests for EntityHeadersModel serialization aliases."""

    def test_all_headers_with_serialization_aliases(self):
        """Test that all headers are serialized with correct aliases."""
        headers = EntityHeadersModel(
            content_type="application/json",
            content_length=2048,
            content_encoding="gzip",
            content_language="es",
        )

        serialized = headers.model_dump(by_alias=True)
        assert serialized["Content-Type"] == "application/json"
        assert serialized["Content-Length"] == 2048
        assert serialized["Content-Encoding"] == "gzip"
        assert serialized["Content-Language"] == "es"

    def test_optional_headers_default_to_none(self):
        """Test that optional headers default to None."""
        headers = EntityHeadersModel()
        assert headers.content_type is None
        assert headers.content_length is None
        assert headers.content_encoding is None
        assert headers.content_language is None

        serialized = headers.model_dump(by_alias=True)
        assert all(v is None for v in serialized.values())


class TestRequestHeadersModel:
    """Tests for RequestHeadersModel."""

    def test_request_headers_serialization_aliases(self):
        """Test that RequestHeadersModel preserves serialization aliases."""
        headers = RequestHeadersModel(
            content_type="application/json",
            content_length=2048,
            content_encoding="gzip",
            content_language="es",
        )

        serialized = headers.model_dump(by_alias=True)
        assert serialized["Content-Type"] == "application/json"
        assert serialized["Content-Length"] == 2048
        assert serialized["Content-Encoding"] == "gzip"
        assert serialized["Content-Language"] == "es"


class TestRequestModelEndpointValidation:
    """Tests for RequestModel endpoint-based URL construction."""

    def test_request_model_with_nested_endpoint(self):
        """Test RequestModel with nested endpoint path."""
        request = RequestModel[None, None](
            endpoint="users/user123/playlists",
            method_type=HTTPMethod.GET,
        )

        assert request.method_type is HTTPMethod.GET
        assert request.endpoint == "users/user123/playlists"
        assert str(request.url) == str(API_BASE_URL / "users/user123/playlists")

    def test_request_model_url_priority_over_endpoint(self):
        """Test that explicit URL takes priority over endpoint."""
        url = HttpUrl(f"{API_BASE_URL}custom/endpoint")
        request = RequestModel[None, None](
            url=url,
            endpoint="me",
            method_type=HTTPMethod.GET,
        )

        assert request.url == url
        assert request.endpoint == "me"

    def test_request_model_raises_when_neither_url_nor_endpoint(self):
        """Test that ValueError is raised when neither url nor endpoint is provided."""
        with pytest.raises(ValidationError):
            RequestModel[None, None](
                method_type=HTTPMethod.GET,
            )

    def test_request_model_raises_for_invalid_url(self):
        """Test that ValueError is raised for URLs not starting with API base."""
        with pytest.raises(ValidationError):
            RequestModel[None, None](
                url=HttpUrl("https://example.com/endpoint"),
                method_type=HTTPMethod.GET,
            )


class TestRequestModelHeaders:
    """Tests for RequestModel headers."""

    def test_request_model_with_custom_headers(self):
        """Test RequestModel with custom headers."""
        headers = RequestHeadersModel(content_type="application/json")
        request = RequestModel[None, None](
            endpoint="me",
            method_type=HTTPMethod.GET,
            headers=headers,
        )

        assert request.headers.content_type == "application/json"
        serialized = request.headers.model_dump(by_alias=True)
        assert serialized["Content-Type"] == "application/json"


class TestRequestModelScopes:
    """Tests for RequestModel required_scopes."""

    def test_request_model_empty_scopes_by_default(self):
        """Test that required_scopes defaults to empty set."""
        request = RequestModel[None, None](
            endpoint="me",
            method_type=HTTPMethod.GET,
        )

        assert request.required_scopes == set()

    def test_request_model_with_required_scopes(self):
        """Test RequestModel with required scopes."""
        scopes = {AuthScope.USER_READ_EMAIL, AuthScope.USER_READ_PRIVATE}
        request = RequestModel[None, None](
            endpoint="me",
            method_type=HTTPMethod.GET,
            required_scopes=scopes,
        )

        assert request.required_scopes == scopes


class TestRequestModelGenericParameters:
    """Tests for RequestModel generic parameters (params and body)."""

    def test_request_model_with_pydantic_params_model(self):
        """Test RequestModel with Pydantic BaseModel params."""

        class CustomParams(BaseModel):
            limit: int = 10
            offset: int = 0

        params = CustomParams(limit=20, offset=5)
        request = RequestModel[CustomParams, None](
            endpoint="me",
            method_type=HTTPMethod.GET,
            params=params,
        )

        assert isinstance(request.params, CustomParams)
        assert request.params.limit == 20
        assert request.params.offset == 5

    def test_request_model_with_request_body_json_model(self):
        """Test RequestModel with RequestBodyJsonModel body."""

        class CustomBody(RequestBodyJsonModel):
            name: str
            description: str

        body = CustomBody(name="Test", description="Test body")
        request = RequestModel[None, CustomBody](
            endpoint="me",
            method_type=HTTPMethod.POST,
            body=body,
        )

        assert isinstance(request.body, CustomBody)
        assert request.body.name == "Test"
        assert request.body.description == "Test body"
        assert request.body.to_http_body() == request.body.model_dump_json(exclude_none=True)


class TestRequestModelHTTPMethods:
    """Tests for RequestModel HTTP method types."""

    @pytest.mark.parametrize("method", [HTTPMethod.GET, HTTPMethod.POST, HTTPMethod.PUT, HTTPMethod.DELETE])
    def test_request_model_with_various_http_methods(self, method):
        """Test RequestModel with various HTTP methods."""
        request = RequestModel[None, None](
            endpoint="me",
            method_type=method,
        )

        assert request.method_type is method


class TestRequestModelValidation:
    """Tests for RequestModel validation logic."""

    def test_request_model_invalid_url(self):
        """Test that RequestModel raises ValidationError for invalid URL."""
        with pytest.raises(ValidationError):
            RequestModel[None, None](
                url=HttpUrl("https://invalid.com/endpoint"),
                method_type=HTTPMethod.GET,
            )

    def test_request_model_missing_url_and_endpoint(self):
        """Test that RequestModel raises ValidationError when both url and endpoint are missing."""
        with pytest.raises(ValidationError):
            RequestModel[None, None](
                method_type=HTTPMethod.GET,
            )


class TestRequestModelToHttpRequestKwargs:
    """Tests for RequestModel _to_http_request_kwargs method."""

    def test_request_model_to_http_request_kwargs(self):
        """Test that _to_http_request_kwargs returns correct data for HTTP request."""

        class CustomParams(BaseModel):
            limit: int = 10
            offset: int = 0

        class CustomBody(RequestBodyJsonModel):
            name: str
            description: str

        headers = RequestHeadersModel(content_type="application/json")
        params = CustomParams(limit=20, offset=5)
        body = CustomBody(name="Test", description="Test body")
        request = RequestModel[CustomParams, CustomBody](
            endpoint="me",
            method_type=HTTPMethod.GET,
            headers=headers,
            params=params,
            body=body,
        )

        auth_header = {"Authorization": "Bearer token"}
        http_kwargs = request._to_http_request_kwargs(auth_headers=auth_header)

        assert http_kwargs["method"] == "GET"
        assert http_kwargs["url"] == str(API_BASE_URL / "me")
        assert http_kwargs["headers"]["Content-Type"] == "application/json"
        assert http_kwargs["headers"]["Authorization"] == "Bearer token"
        assert http_kwargs["params"] == {"limit": 20, "offset": 5}
        assert http_kwargs["data"] == body.to_http_body()
