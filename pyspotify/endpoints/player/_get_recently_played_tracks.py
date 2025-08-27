from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.models import APICallModel
from pyspotify.models.player.requests import GetRecentlyPlayedTracksRequest
from pyspotify.models.player.requests import GetRecentlyPlayedTracksRequestParams
from pyspotify.models.spotify import PagedResultWithCursorsModel
from pyspotify.models.spotify import PlayHistoryModel


async def get_recently_played_tracks(
    client: PySpotifyClient, *, limit: int = 20, after: Optional[int] = None, before: Optional[int] = None
) -> APICallModel[GetRecentlyPlayedTracksRequest, APIResponse, PagedResultWithCursorsModel[PlayHistoryModel]]:
    request = GetRecentlyPlayedTracksRequest(
        endpoint="me/player/recently-played",
        params=GetRecentlyPlayedTracksRequestParams(
            limit=limit,
            after=after,
            before=before,
        ),
    )
    response = await client.request(request)
    assert response is not None
    data = PagedResultWithCursorsModel[PlayHistoryModel](**response)

    return APICallModel(request=request, response=response, data=data)
