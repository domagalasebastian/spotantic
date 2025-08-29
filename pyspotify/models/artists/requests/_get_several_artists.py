from http import HTTPMethod
from typing import Annotated
from typing import Sequence

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import PlainSerializer

from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import RequestModel


class GetSeveralArtistsRequestParams(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    artist_ids: Annotated[
        Sequence[SpotifyItemID],
        Field(max_length=50, serialization_alias="ids"),
        PlainSerializer(lambda seq: ",".join(seq), return_type=str),
    ]


class GetSeveralArtistsRequest(RequestModel[GetSeveralArtistsRequestParams, None]):
    method_type: HTTPMethod = HTTPMethod.GET
