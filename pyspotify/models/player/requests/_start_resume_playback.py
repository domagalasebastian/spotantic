from __future__ import annotations

from http import HTTPMethod
from typing import Annotated
from typing import Optional
from typing import Sequence
from typing import Union

from pydantic import BaseModel
from pydantic import Field
from pydantic import model_validator

from pyspotify.custom_types import SpotifyAlbumURI
from pyspotify.custom_types import SpotifyArtistURI
from pyspotify.custom_types import SpotifyPlaylistURI
from pyspotify.custom_types import SpotifyTrackURI
from pyspotify.models import RequestModel


class PositionOffsetModel(BaseModel):
    position: Annotated[int, Field(ge=0)]


class URIOffsetModel(BaseModel):
    uri: SpotifyTrackURI


class StartResumePlaybackRequestParams(BaseModel):
    device_id: Optional[str] = None


class StartResumePlaybackRequestBody(BaseModel):
    context_uri: Optional[Union[SpotifyAlbumURI, SpotifyArtistURI, SpotifyPlaylistURI]] = None
    uris: Optional[Sequence[SpotifyTrackURI]] = None
    offset: Optional[Union[PositionOffsetModel, URIOffsetModel]] = None
    position_ms: Optional[int] = None

    @model_validator(mode="after")
    def validate_body_data(self) -> StartResumePlaybackRequestBody:
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
    method_type: HTTPMethod = HTTPMethod.PUT
