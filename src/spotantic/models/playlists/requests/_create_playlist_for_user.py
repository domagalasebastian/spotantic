from __future__ import annotations

from http import HTTPMethod
from typing import Optional

from pydantic import BaseModel
from pydantic import model_validator

from spotantic.models import RequestBodyJsonModel
from spotantic.models import RequestHeadersModel
from spotantic.models import RequestModel
from spotantic.types import AuthScope


class CreatePlaylistForUserRequestParams(BaseModel):
    """Params model for Create Playlist For User request."""

    user_id: str
    """The Spotify user ID of the playlist owner."""


class CreatePlaylistForUserRequestBody(RequestBodyJsonModel):
    """Body model for Create Playlist For User request."""

    name: str
    """The name for the new playlist."""

    public: Optional[bool] = None
    """Whether the playlist should be public."""

    collaborative: Optional[bool] = None
    """Whether the playlist should be collaborative."""

    description: Optional[str] = None
    """The description for the new playlist."""

    @model_validator(mode="after")
    def validate_flags(self) -> CreatePlaylistForUserRequestBody:
        """Validates the `public` and `collaborative` flags.

        Returns:
            The validated model.

        Raises:
            ValueError: If `public` is False and `collaborative` is True.
        """
        if self.public is False and self.collaborative is True:
            raise ValueError("To create a collaborative playlist you must also set `public` to False!")

        return self


class CreatePlaylistForUserRequest(RequestModel[CreatePlaylistForUserRequestParams, CreatePlaylistForUserRequestBody]):
    """Request model for Create Playlist For User endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.PLAYLIST_MODIFY_PRIVATE, AuthScope.PLAYLIST_MODIFY_PUBLIC}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.POST
    """HTTP method for the request."""

    headers: RequestHeadersModel = RequestHeadersModel(content_type="application/json")
    """Headers for the request."""

    @classmethod
    def build(
        cls,
        *,
        user_id: str,
        name: str,
        description: Optional[str] = None,
        public: Optional[bool] = None,
        collaborative: Optional[bool] = None,
    ) -> CreatePlaylistForUserRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            user_id: The Spotify user ID of the playlist owner.
            name: The name for the new playlist.
            description: The description for the new playlist.
            public: Whether the playlist should be public.
            collaborative: Whether the playlist should be collaborative.

        Returns:
            Validated Request object.
        """
        params = CreatePlaylistForUserRequestParams(user_id=user_id)
        body = CreatePlaylistForUserRequestBody(
            name=name,
            public=public,
            collaborative=collaborative,
            description=description,
        )
        endpoint = f"users/{user_id}/playlists"

        return cls(endpoint=endpoint, params=params, body=body)
