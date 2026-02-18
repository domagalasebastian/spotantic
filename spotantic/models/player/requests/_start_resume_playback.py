from __future__ import annotations

from http import HTTPMethod
from typing import Annotated
from typing import Optional
from typing import Sequence
from typing import Union

from pydantic import BaseModel
from pydantic import Field
from pydantic import model_validator

from spotantic.models import RequestHeadersModel
from spotantic.models import RequestModel
from spotantic.types import AuthScope
from spotantic.types import SpotifyAlbumURI
from spotantic.types import SpotifyArtistURI
from spotantic.types import SpotifyPlaylistURI
from spotantic.types import SpotifyTrackURI


class PositionOffsetModel(BaseModel):
    """Offset model based on position index."""

    position: Annotated[int, Field(ge=0)]
    """Indicates the position in milliseconds to start playback."""


class URIOffsetModel(BaseModel):
    """Offset model based on Spotify track URI."""

    uri: SpotifyTrackURI
    """Spotify track URI to start playback from."""


class StartResumePlaybackRequestParams(BaseModel):
    """Params model for Start/Resume Playback request."""

    device_id: Optional[str] = None
    """The id of the device this command is targeting."""


class StartResumePlaybackRequestBody(BaseModel):
    """Body model for Start/Resume Playback request."""

    context_uri: Optional[Union[SpotifyAlbumURI, SpotifyArtistURI, SpotifyPlaylistURI]] = None
    """Spotify URI of the context to play."""

    uris: Optional[Sequence[SpotifyTrackURI]] = None
    """A list of Spotify track URIs to play."""

    offset: Optional[Union[PositionOffsetModel, URIOffsetModel]] = None
    """Indicates from where in the context playback should start."""

    position_ms: Optional[int] = None
    """Indicates the position in milliseconds to start playback."""

    @model_validator(mode="after")
    def validate_body_data(self) -> StartResumePlaybackRequestBody:
        """Validates the body data according to Spotify API rules.

        Returns:
            The validated body model instance.

        Raises:
            ValueError: If validation fails.
        """
        if self.context_uri is not None and self.uris is not None:
            raise ValueError("Specify either a `context_uri` or `uris` parameter, but not both!")

        if self.offset is not None:
            if self.context_uri is None and self.uris is None:
                raise ValueError("Offset without `context_uri` or `uris` not allowed!")

            if not isinstance(self.context_uri, Optional[Union[SpotifyAlbumURI, SpotifyPlaylistURI]]):
                raise ValueError("Offset is available when `context_uri` corresponds to an album or playlist object!")

            if self.uris is not None:
                if isinstance(self.offset, PositionOffsetModel) and self.offset.position > len(self.uris):
                    raise ValueError("Provided `offset` position exceeds provided `uris` list length!")

                if isinstance(self.offset, URIOffsetModel) and self.offset.uri not in self.uris:
                    raise ValueError("Provided `offset` URI is not in `uris` list!")

        return self


class StartResumePlaybackRequest(RequestModel[StartResumePlaybackRequestParams, StartResumePlaybackRequestBody]):
    """Request model for Start/Resume Playback endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.USER_MODIFY_PLAYBACK_STATE}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.PUT
    """HTTP method for the request."""

    endpoint: Optional[str] = "me/player/play"
    """Endpoint associated with the request."""

    headers: RequestHeadersModel = RequestHeadersModel(content_type="application/json")
    """Headers for the request."""

    @classmethod
    def build(
        cls,
        *,
        device_id: Optional[str] = None,
        context_uri: Optional[Union[SpotifyAlbumURI, SpotifyArtistURI, SpotifyPlaylistURI]] = None,
        uris: Optional[Sequence[SpotifyTrackURI]] = None,
        offset: Optional[Union[int, SpotifyTrackURI]] = None,
        position_ms: Optional[int] = None,
    ) -> StartResumePlaybackRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            device_id: The id of the device this command is targeting.
            context_uri: Spotify URI of the context to play.
            uris: A list of Spotify track URIs to play.
            offset: Indicates from where in the context playback should start.
            position_ms: Indicates the position in milliseconds to start playback.

        Returns:
            Validated Request object.
        """
        params = StartResumePlaybackRequestParams(
            device_id=device_id,
        )

        if offset is None:
            offset_model = None
        elif isinstance(offset, int):
            offset_model = PositionOffsetModel(position=offset)
        else:
            offset_model = URIOffsetModel(uri=offset)

        body = StartResumePlaybackRequestBody(
            context_uri=context_uri,
            uris=uris,
            offset=offset_model,
            position_ms=position_ms,
        )

        return cls(params=params, body=body)
