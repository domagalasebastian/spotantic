from typing import Sequence

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.users.requests import UnfollowArtistsOrUsersRequest
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemType


async def unfollow_artists_or_users(
    client: SpotanticClient,
    *,
    item_type: SpotifyItemType,
    item_ids: Sequence[str],
) -> APICallModel[UnfollowArtistsOrUsersRequest, APIResponse, None]:
    """Unfollow artists or users on behalf of the current user.

    Remove the current user as a follower of one or more artists or other Spotify users.

    Args:
        client: An instance of `SpotanticClient`.
        item_type: The type of the items to unfollow. Must be either 'artist' or 'user'.
        item_ids: A sequence of Spotify IDs for the artists or users to unfollow. Maximum of 50 IDs.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = UnfollowArtistsOrUsersRequest.build(
        item_type=item_type,
        item_ids=item_ids,
    )
    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
