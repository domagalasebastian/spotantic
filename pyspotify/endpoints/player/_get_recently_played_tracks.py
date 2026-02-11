from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.models import APICallModel
from pyspotify.models.player.requests import GetRecentlyPlayedTracksRequest
from pyspotify.models.spotify import PagedResultWithCursorsModel
from pyspotify.models.spotify import PlayHistoryModel
from pyspotify.types import APIResponse


async def get_recently_played_tracks(
    client: PySpotifyClient, *, limit: int = 20, after: Optional[int] = None, before: Optional[int] = None
) -> APICallModel[GetRecentlyPlayedTracksRequest, APIResponse, PagedResultWithCursorsModel[PlayHistoryModel]]:
    """Get the user's recently played tracks.

    Get tracks from the current user's recently played tracks.

    Args:
        client: PySpotifyClient instance.
        limit: The maximum number of items to return. Default is 20. Minimum is 1, maximum is 50.
        after: A Unix timestamp in milliseconds. Returns all items after (but not including) this cursor position.
        before: A Unix timestamp in milliseconds. Returns all items before (but not including) this cursor position.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetRecentlyPlayedTracksRequest.build(limit=limit, after=after, before=before)
    response = await client.request(request)
    assert response is not None
    data = PagedResultWithCursorsModel[PlayHistoryModel](**response)

    return APICallModel(request=request, response=response, data=data)
