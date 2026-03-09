from typing import Optional

from pydantic import BaseModel
from pydantic import HttpUrl
from pydantic import SecretStr
from pydantic import field_serializer

from spotantic._utils.models._custom_serializers import secret_str_to_str


class AuthCodeRequestParams(BaseModel):
    """Params model for the User Authorization Request."""

    client_id: SecretStr
    """The Client ID generated after registering your application."""

    response_type: str
    """A response type."""

    redirect_uri: HttpUrl
    """The URI to redirect to after the user grants or denies permission."""

    scope: str
    """A space-separated list of scopes which have been granted for this access_token."""

    code_challenge_method: Optional[str] = None
    """A code challenge method."""

    code_challenge: Optional[str] = None
    """Set to the code challenge that your app calculated based on the code verifier."""

    @field_serializer("client_id", when_used="json")
    def dump_secret_value(self, secret_val: SecretStr) -> str:
        """Dumps a secret value to plain str.

        Args:
            secret_val: Secret string.

        Returns:
            The same string in the plain-text form.
        """
        return secret_str_to_str(secret_val)
