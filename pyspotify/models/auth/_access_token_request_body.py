from typing import Optional

from pydantic import BaseModel
from pydantic import HttpUrl


class AccessTokenRequestBody(BaseModel):
    """Body model for obtaining/refreshing an access token."""

    grant_type: str
    """A grant type."""

    code: Optional[str] = None
    """The authorization code returned from the User Authorization request."""

    redirect_uri: Optional[HttpUrl] = None
    """This parameter is used for validation only."""

    client_id: Optional[str] = None
    """The Client ID generated after registering your application."""

    code_verifier: Optional[str] = None
    """A code verifier matching the code challenge used to obtain the `code`"""

    refresh_token: Optional[str] = None
    """The refresh token returned from the authorization token request."""
