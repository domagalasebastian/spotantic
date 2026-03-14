from http import HTTPMethod

import pytest
from pydantic import BaseModel
from pydantic import HttpUrl
from pydantic import ValidationError

from spotantic.models._request_model import API_BASE_URL
from spotantic.models._request_model import EntityHeadersModel
from spotantic.models._request_model import RequestHeadersModel
from spotantic.models._request_model import RequestModel
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

    def test_request_model_with_pydantic_body_model(self):
        """Test RequestModel with Pydantic BaseModel body."""

        class CustomBody(BaseModel):
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
