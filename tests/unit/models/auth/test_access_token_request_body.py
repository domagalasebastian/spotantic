from pydantic import HttpUrl
from pydantic import SecretStr

from spotantic.models.auth import AccessTokenRequestBody


def test_access_token_request_body_authorization_code_flow():
    """Test AccessTokenRequestBody for authorization code flow."""
    redirect_uri = HttpUrl("http://localhost:8000/callback")
    body = AccessTokenRequestBody(
        grant_type="authorization_code",
        code="auth_code_123",
        redirect_uri=redirect_uri,
        client_id=SecretStr("client_id_123"),
    )

    assert body.grant_type == "authorization_code"
    assert body.code == "auth_code_123"
    assert body.redirect_uri == redirect_uri
    assert body.client_id is not None
    assert body.client_id.get_secret_value() == "client_id_123"
    assert body.code_verifier is None
    assert body.refresh_token is None


def test_access_token_request_body_refresh_token_flow():
    """Test AccessTokenRequestBody for refresh token flow."""
    body = AccessTokenRequestBody(
        grant_type="refresh_token",
        refresh_token=SecretStr("refresh_token_123"),
        client_id=SecretStr("client_id_123"),
    )

    assert body.grant_type == "refresh_token"
    assert body.refresh_token is not None
    assert body.refresh_token.get_secret_value() == "refresh_token_123"
    assert body.client_id is not None
    assert body.client_id.get_secret_value() == "client_id_123"
    assert body.code is None
    assert body.redirect_uri is None
    assert body.code_verifier is None


def test_access_token_request_body_client_credentials_flow():
    """Test AccessTokenRequestBody for client credentials flow."""
    body = AccessTokenRequestBody(
        grant_type="client_credentials",
        client_id=SecretStr("client_id_123"),
    )

    assert body.grant_type == "client_credentials"
    assert body.client_id is not None
    assert body.client_id.get_secret_value() == "client_id_123"
    assert body.code is None
    assert body.redirect_uri is None
    assert body.refresh_token is None
    assert body.code_verifier is None


def test_access_token_request_body_pkce_flow():
    """Test AccessTokenRequestBody for PKCE flow."""
    body = AccessTokenRequestBody(
        grant_type="authorization_code",
        code="auth_code_123",
        code_verifier="code_verifier_123",
        redirect_uri=HttpUrl("http://localhost:8000/callback"),
        client_id=SecretStr("client_id_123"),
    )

    assert body.grant_type == "authorization_code"
    assert body.code == "auth_code_123"
    assert body.code_verifier == "code_verifier_123"
    assert body.redirect_uri == HttpUrl("http://localhost:8000/callback")
    assert body.client_id is not None
    assert body.client_id.get_secret_value() == "client_id_123"


def test_access_token_request_body_serialization():
    """Test AccessTokenRequestBody serialization to dict."""
    body = AccessTokenRequestBody(
        grant_type="authorization_code",
        code="auth_code_123",
        redirect_uri=HttpUrl("http://localhost:8000/callback"),
        client_id=SecretStr("client_id_123"),
    )

    data = body.model_dump(by_alias=True, mode="json")
    assert data["grant_type"] == "authorization_code"
    assert data["code"] == "auth_code_123"
    assert data["client_id"] == "client_id_123"
    assert data["redirect_uri"] == "http://localhost:8000/callback"


def test_access_token_request_body_all_optional_fields():
    """Test AccessTokenRequestBody with all optional fields None."""
    body = AccessTokenRequestBody(
        grant_type="client_credentials",
    )

    assert body.grant_type == "client_credentials"
    assert body.code is None
    assert body.redirect_uri is None
    assert body.client_id is None
    assert body.code_verifier is None
    assert body.refresh_token is None
