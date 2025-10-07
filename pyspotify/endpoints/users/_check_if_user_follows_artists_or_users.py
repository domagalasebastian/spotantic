from typing import Dict
from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyItemType
from pyspotify.models import APICallModel
from pyspotify.models.users.requests import CheckIfUserFollowsArtistsOrUsersRequest


async def check_if_user_follows_artists_or_users(
    client: PySpotifyClient,
    *,
    item_type: SpotifyItemType,
    item_ids: Sequence[str],
) -> APICallModel[CheckIfUserFollowsArtistsOrUsersRequest, APIResponse, Dict[SpotifyItemID, bool]]:
    request = CheckIfUserFollowsArtistsOrUsersRequest.build(
        item_type=item_type,
        item_ids=item_ids,
    )
    response = await client.request(request)
    assert response is not None
    data = dict(zip(item_ids, response))

    return APICallModel(request=request, response=response, data=data)
