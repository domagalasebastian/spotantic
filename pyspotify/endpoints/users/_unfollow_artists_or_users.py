from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemType
from pyspotify.models import APICallModel
from pyspotify.models.users.requests import UnfollowArtistsOrUsersRequest


async def unfollow_artists_or_users(
    client: PySpotifyClient,
    *,
    item_type: SpotifyItemType,
    item_ids: Sequence[str],
) -> APICallModel[UnfollowArtistsOrUsersRequest, APIResponse, None]:
    request = UnfollowArtistsOrUsersRequest.build(
        item_type=item_type,
        item_ids=item_ids,
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
