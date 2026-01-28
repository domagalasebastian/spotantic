from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyItemType
from pyspotify.models import APICallModel
from pyspotify.models.users.requests import FollowArtistsOrUsersRequest


async def follow_artists_or_users(
    client: PySpotifyClient,
    *,
    item_type: SpotifyItemType,
    item_ids: Sequence[SpotifyItemID],
) -> APICallModel[FollowArtistsOrUsersRequest, APIResponse, None]:
    """Follow one or more artists or Spotify users.

    Add the current user as a follower of one or more artists or other Spotify users.

    Args:
        client: PySpotifyClient instance.
        item_type: The type of item to follow.
        item_ids: A list of Spotify IDs for the artists or users to follow.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = FollowArtistsOrUsersRequest.build(
        item_type=item_type,
        item_ids=item_ids,
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
