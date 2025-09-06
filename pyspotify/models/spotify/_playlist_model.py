from typing import Literal
from typing import Optional
from typing import Sequence

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl

from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyPlaylistURI
from pyspotify.custom_types import SpotifyUserURI
from pyspotify.models.spotify._image_model import ImageModel
from pyspotify.models.spotify._paged_result_model import PagedResultModel
from pyspotify.models.spotify._playlist_track_model import PlaylistTrackModel


class ExternalUrlsModel(BaseModel):
    spotify: Optional[HttpUrl] = None


class OwnerModel(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    external_urls: ExternalUrlsModel = Field(repr=False)
    user_href: HttpUrl = Field(alias="href")
    user_id: str = Field(alias="id")
    item_type: Literal["user"] = Field(alias="type", repr=False)
    user_uri: SpotifyUserURI = Field(alias="uri", repr=False)
    display_name: Optional[str] = None


class PlaylistBaseModel(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    collaborative: bool = Field(repr=False)
    description: Optional[str] = None
    external_urls: ExternalUrlsModel = Field(repr=False)
    playlist_href: HttpUrl = Field(alias="href")
    playlist_id: SpotifyItemID = Field(alias="id", repr=False)
    images: Sequence[ImageModel] = Field(repr=False)
    playlist_name: str = Field(alias="name")
    owner: OwnerModel
    public: Optional[bool] = Field(None, repr=False)
    snapshot_id: str
    item_type: Literal["playlist"] = Field(alias="type", repr=False)
    playlist_uri: SpotifyPlaylistURI = Field(alias="uri", repr=False)


class PlaylistModel(PlaylistBaseModel):
    tracks: PagedResultModel[PlaylistTrackModel]


class PlaylistSummaryModel(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    tracks_href: HttpUrl = Field(alias="href")
    tracks_total: int = Field(alias="total")


class SimplifiedPlaylistModel(PlaylistBaseModel):
    tracks: Optional[PlaylistSummaryModel] = None
