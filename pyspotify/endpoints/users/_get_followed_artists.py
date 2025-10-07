from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyItemType
from pyspotify.models import APICallModel
from pyspotify.models.spotify import ArtistModel
from pyspotify.models.spotify import PagedResultWithCursorsModel
from pyspotify.models.users.requests import GetFollowedArtistsRequest


async def get_followed_artists(
    client: PySpotifyClient,
    *,
    item_type: SpotifyItemType = SpotifyItemType.ARTIST,
    after: Optional[SpotifyItemID] = None,
    limit: Optional[int] = 20,
) -> APICallModel[GetFollowedArtistsRequest, APIResponse, PagedResultWithCursorsModel[ArtistModel]]:
    request = GetFollowedArtistsRequest.build(
        item_type=item_type,
        after=after,
        limit=limit,
    )
    response = await client.request(request)
    assert response is not None
    data = PagedResultWithCursorsModel[ArtistModel](**response["artists"])

    return APICallModel(request=request, response=response, data=data)
