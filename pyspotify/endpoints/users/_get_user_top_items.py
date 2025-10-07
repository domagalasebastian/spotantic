from typing import Union

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.models import APICallModel
from pyspotify.models.spotify import ArtistModel
from pyspotify.models.spotify import PagedResultModel
from pyspotify.models.spotify import TrackModel
from pyspotify.models.users.requests import GetUserTopItemsRequest
from pyspotify.models.users.requests import GetUserTopItemsTimeRange
from pyspotify.models.users.requests import GetUserTopItemsType


async def get_user_top_items(
    client: PySpotifyClient,
    *,
    item_type: GetUserTopItemsType,
    time_range: GetUserTopItemsTimeRange,
    limit: int = 20,
    offset: int = 0,
) -> APICallModel[
    GetUserTopItemsRequest, APIResponse, Union[PagedResultModel[ArtistModel], PagedResultModel[TrackModel]]
]:
    request = GetUserTopItemsRequest.build(
        item_type=item_type,
        time_range=time_range,
        limit=limit,
        offset=offset,
    )
    response = await client.request(request)
    assert response is not None
    match item_type:
        case GetUserTopItemsType.ARTISTS:
            data = PagedResultModel[ArtistModel](**response)
        case GetUserTopItemsType.TRACKS:
            data = PagedResultModel[TrackModel](**response)

    return APICallModel(request=request, response=response, data=data)
