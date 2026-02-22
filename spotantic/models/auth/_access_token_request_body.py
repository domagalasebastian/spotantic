from typing import Optional

from pydantic import BaseModel
from pydantic import HttpUrl
from pydantic import SecretStr
from pydantic import field_serializer

from spotantic._utils.models._custom_serializers import secret_str_to_str


class AccessTokenRequestBody(BaseModel):
    """Body model for obtaining/refreshing an access token."""

    grant_type: str
    """A grant type."""

    code: Optional[str] = None
    """The authorization code returned from the User Authorization request."""

    redirect_uri: Optional[HttpUrl] = None
    """This parameter is used for validation only."""

    client_id: Optional[SecretStr] = None
    """The Client ID generated after registering your application."""

    code_verifier: Optional[str] = None
    """A code verifier matching the code challenge used to obtain the `code`"""

    refresh_token: Optional[SecretStr] = None
    """The refresh token returned from the authorization token request."""

    @field_serializer("client_id", "refresh_token", when_used="json-unless-none")
    def dump_secret_value(self, secret_val: SecretStr) -> str:
        """Dumps a secret value to plain str.

        Args:
            secret_val: Secret string.

        Returns:
            The same string in the plain-text form.
        """
        return secret_str_to_str(secret_val)
