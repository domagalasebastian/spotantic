from typing import Optional

from pydantic import BaseModel
from pydantic import HttpUrl


class AuthCodeRequestParams(BaseModel):
    """Params model for the User Authorization Request."""

    client_id: str
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
