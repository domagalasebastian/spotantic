from __future__ import annotations

from datetime import datetime
from datetime import timedelta
from pathlib import Path
from typing import Any
from typing import Literal
from typing import Optional

from pydantic import BaseModel
from pydantic import SecretStr
from pydantic import field_serializer

from spotantic._utils.models._custom_serializers import secret_str_to_str


class AccessTokenInfo(BaseModel):
    """Model representing information about an access token."""

    access_token: SecretStr
    """An access token that can be provided in subsequent calls, for example to Spotify Web API services."""

    token_type: Literal["Bearer"]
    """How the access token may be used (always `Bearer`)."""

    scope: Optional[str] = None
    """A space-separated list of scopes which have been granted for this access_token."""

    expires_in: int
    """The time period (in seconds) for which the access token is valid."""

    refresh_token: Optional[SecretStr] = None
    """A security credential that allows client applications to obtain new access tokens
    without requiring users to reauthorize the application."""

    expires_at: Optional[datetime] = None
    """Datetime object informing when the token expires."""

    @field_serializer("access_token", "refresh_token", when_used="json-unless-none")
    def dump_secret_value(self, secret_val: SecretStr) -> str:
        """Dumps a secret value to plain str.

        Args:
            secret_val: Secret string.

        Returns:
            The same string in the plain-text form.
        """
        return secret_str_to_str(secret_val)

    def model_post_init(self, context: Any, /) -> None:
        """Set `expires_at` when not provided, assuming this is a new access token.

        Args:
            context: Model context.

        Returns:
            None
        """
        if self.expires_at is None:
            self.expires_at = datetime.now() + timedelta(seconds=self.expires_in)

        return super().model_post_init(context)

    def store_token(self, file_path: Path) -> None:
        """Dumps the access token info into a file.

        Args:
            file_path: File location to save the access token at.

        Returns:
            None
        """
        with open(file_path, "w") as fd:
            fd.write(self.model_dump_json())

    @classmethod
    def load_token(cls, file_path: Path) -> AccessTokenInfo:
        """Loads the access token info from a file.

        Args:
            file_path: File location to load the access token from.

        Returns:
            Validated model instance.
        """
        with open(file_path, "r") as fd:
            json_data = fd.read()

        return cls.model_validate_json(json_data=json_data)

    def is_expired(self) -> bool:
        """Checks if the token is expired.

        Returns:
            ``True`` if the token is expired, ``False`` otherwise.

        Raises:
            ValueError: If ``expires_at`` is not set.
        """
        if self.expires_at is None:
            raise ValueError("Token 'expires_at' is not set; cannot determine expiration.")

        return datetime.now() >= self.expires_at

    def get_authorization_header(self) -> dict[str, str]:
        """Return the `Authorization` header.

        The header value is constructed as "{token_type} {access_token}".

        Returns:
            Authorization header for API calls.
        """
        return {"Authorization": f"{self.token_type} {self.access_token.get_secret_value()}"}
