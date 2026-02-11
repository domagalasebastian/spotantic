from __future__ import annotations

from datetime import datetime
from datetime import timedelta
from pathlib import Path
from typing import Any
from typing import Literal
from typing import Optional

from pydantic import BaseModel


class AccessTokenInfo(BaseModel):
    """Model representing information about an access token."""

    access_token: str
    """An access token that can be provided in subsequent calls, for example to Spotify Web API services."""

    token_type: Literal["Bearer"]
    """How the access token may be used (always `Bearer`)."""

    scope: Optional[str] = None
    """A space-separated list of scopes which have been granted for this access_token."""

    expires_in: int
    """The time period (in seconds) for which the access token is valid."""

    refresh_token: Optional[str] = None
    """A security credential that allows client applications to obtain new access tokens
    without requiring users to reauthorize the application."""

    expires_at: Optional[datetime] = None
    """Datetime object informing when the token expires."""

    def model_post_init(self, context: Any, /) -> None:
        """Sets `expires_at` attribute with an assumption it is a new access token.

        Args
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
