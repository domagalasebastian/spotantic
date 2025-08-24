from datetime import timedelta
from typing import Literal
from typing import Optional
from typing import Sequence

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl
from pydantic import field_validator

from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.custom_types import SpotifyTrackURI
from pyspotify.models.spotify._simplified_artist_model import SimplifiedArtistModel


class ExternalUrlsModel(BaseModel):
    spotify: Optional[HttpUrl] = None


class RestrictionsModel(BaseModel):
    reason: Optional[Literal["market", "product", "explicit"]] = None


class LinkedFromModel(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    external_urls: ExternalUrlsModel = Field(repr=False)
    track_href: HttpUrl = Field(alias="href")
    track_id: SpotifyItemID = Field(alias="id", repr=False)
    item_type: Literal["track"] = Field(alias="type", repr=False)
    track_uri: SpotifyTrackURI = Field(alias="uri", repr=False)


class SimplifiedTrackModel(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    artists: Sequence[SimplifiedArtistModel]
    available_markets: Sequence[SpotifyMarketID] = Field(repr=False)
    disc_number: int = Field(repr=False)
    duration: timedelta = Field(alias="duration_ms")
    explicit: bool = Field(repr=False)
    external_urls: ExternalUrlsModel = Field(repr=False)
    track_href: HttpUrl = Field(alias="href")
    track_id: SpotifyItemID = Field(alias="id", repr=False)
    is_playable: Optional[bool] = Field(None, repr=False)
    linked_from: Optional[LinkedFromModel] = Field(None, repr=False)
    restrictions: Optional[RestrictionsModel] = Field(None, repr=False)
    track_name: str = Field(alias="name")
    preview_url: Optional[str] = Field(repr=False, deprecated=True)
    track_number: int = Field(repr=False)
    item_type: Literal["track"] = Field(alias="type", repr=False)
    track_uri: SpotifyTrackURI = Field(alias="uri", repr=False)
    is_local: bool = Field(repr=False)

    @field_validator("duration", mode="before")
    def convert_duration_ms_to_timedelta(cls, value: int) -> timedelta:
        return timedelta(milliseconds=value)
