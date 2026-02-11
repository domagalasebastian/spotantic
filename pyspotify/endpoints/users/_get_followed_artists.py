from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.models import APICallModel
from pyspotify.models.spotify import ArtistModel
from pyspotify.models.spotify import PagedResultWithCursorsModel
from pyspotify.models.users.requests import GetFollowedArtistsRequest
from pyspotify.types import APIResponse
from pyspotify.types import SpotifyItemID
from pyspotify.types import SpotifyItemType


async def get_followed_artists(
    client: PySpotifyClient,
    *,
    item_type: SpotifyItemType = SpotifyItemType.ARTIST,
    after: Optional[SpotifyItemID] = None,
    limit: Optional[int] = 20,
) -> APICallModel[GetFollowedArtistsRequest, APIResponse, PagedResultWithCursorsModel[ArtistModel]]:
    """Get the artists followed by the current Spotify user.

    Get the current user's followed artists.

    Args:
        client: PySpotifyClient instance.
        item_type: The ID type: currently only 'artist' is supported.
        after: The last artist ID retrieved from the previous request.
          Used to get the next set of results.
        limit: The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetFollowedArtistsRequest.build(
        item_type=item_type,
        after=after,
        limit=limit,
    )
    response = await client.request(request)
    assert response is not None
    data = PagedResultWithCursorsModel[ArtistModel](**response["artists"])

    return APICallModel(request=request, response=response, data=data)
