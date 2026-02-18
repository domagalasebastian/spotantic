from typing import Sequence

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.users.requests import FollowArtistsOrUsersRequest
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyItemType


async def follow_artists_or_users(
    client: SpotanticClient,
    *,
    item_type: SpotifyItemType,
    item_ids: Sequence[SpotifyItemID],
) -> APICallModel[FollowArtistsOrUsersRequest, APIResponse, None]:
    """Follow one or more artists or Spotify users.

    Add the current user as a follower of one or more artists or other Spotify users.

    Args:
        client: SpotanticClient instance.
        item_type: The type of item to follow.
        item_ids: A list of Spotify IDs for the artists or users to follow.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = FollowArtistsOrUsersRequest.build(
        item_type=item_type,
        item_ids=item_ids,
    )
    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
