from http import HTTPMethod
from typing import Annotated
from typing import Optional
from typing import Sequence

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import PlainSerializer

from pyspotify.custom_types import AlbumTypes
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import RequestModel


class GetArtistAlbumsRequestParams(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True, use_enum_values=True)

    artist_id: SpotifyItemID = Field(serialization_alias="id")
    limit: Annotated[int, Field(ge=1, le=50)]
    offset: int
    include_groups: Annotated[
        Optional[Sequence[AlbumTypes]], PlainSerializer(lambda seq: ",".join(seq), return_type=str)
    ] = None
    market: Optional[SpotifyMarketID] = None


class GetArtistAlbumsRequest(RequestModel[GetArtistAlbumsRequestParams, None]):
    method_type: HTTPMethod = HTTPMethod.GET
