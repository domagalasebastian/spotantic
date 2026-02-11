from typing import Union

from pyspotify.client import PySpotifyClient
from pyspotify.models import APICallModel
from pyspotify.models.spotify import ArtistModel
from pyspotify.models.spotify import PagedResultModel
from pyspotify.models.spotify import TrackModel
from pyspotify.models.users.requests import GetUserTopItemsRequest
from pyspotify.models.users.requests import GetUserTopItemsTimeRange
from pyspotify.models.users.requests import GetUserTopItemsType
from pyspotify.types import APIResponse


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
    """Get the current Spotify user's top artists or tracks.

    Get the current user's top artists or tracks based on calculated affinity.

    Args:
        client: PySpotifyClient instance.
        item_type: The type of item to retrieve (artists or tracks).
        time_range: Over what time frame the affinities are computed.
        limit: The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50.
        offset: The index of the first item to return. Default: 0 (the first item).
          Use with limit to get the next set of items.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
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
