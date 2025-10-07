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
    request = FollowArtistsOrUsersRequest.build(
        item_type=item_type,
        item_ids=item_ids,
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
