from pydantic import HttpUrl
from pydantic import SecretStr

from spotantic.models.auth import AuthCodeRequestParams


def test_auth_code_request_params_valid():
    """Test AuthCodeRequestParams with PKCE parameters."""
    params = AuthCodeRequestParams(
        client_id=SecretStr("client_id_123"),
        response_type="code",
        redirect_uri=HttpUrl("http://localhost:8000/callback"),
        scope="user-read-private",
        code_challenge_method="S256",
        code_challenge="test_challenge_123",
    )

    assert params.client_id.get_secret_value() == "client_id_123"
    assert params.response_type == "code"
    assert params.redirect_uri == HttpUrl("http://localhost:8000/callback")
    assert params.scope == "user-read-private"
    assert params.code_challenge_method == "S256"
    assert params.code_challenge == "test_challenge_123"


def test_auth_code_request_params_serialization():
    """Test AuthCodeRequestParams serialization to dict."""
    params = AuthCodeRequestParams(
        client_id=SecretStr("client_id_123"),
        response_type="code",
        redirect_uri=HttpUrl("http://localhost:8000/callback"),
        scope="user-read-private user-read-email",
        code_challenge_method="S256",
        code_challenge="test_challenge_123",
    )

    data = params.model_dump(by_alias=True, mode="json")
    assert data["client_id"] == "client_id_123"
    assert data["response_type"] == "code"
    assert data["redirect_uri"] == "http://localhost:8000/callback"
    assert data["scope"] == "user-read-private user-read-email"
    assert data["code_challenge_method"] == "S256"
    assert data["code_challenge"] == "test_challenge_123"
