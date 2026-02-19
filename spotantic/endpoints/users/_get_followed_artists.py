from typing import Optional

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.spotify import ArtistModel
from spotantic.models.spotify import PagedResultWithCursorsModel
from spotantic.models.users.requests import GetFollowedArtistsRequest
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyItemType


async def get_followed_artists(
    client: SpotanticClient,
    *,
    item_type: SpotifyItemType = SpotifyItemType.ARTIST,
    after: Optional[SpotifyItemID] = None,
    limit: Optional[int] = 20,
) -> APICallModel[GetFollowedArtistsRequest, APIResponse, PagedResultWithCursorsModel[ArtistModel]]:
    """Get the current user's followed artists.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
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
