from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import APICallModel
from pyspotify.models.albums.requests import RemoveUserSavedAlbumsRequest
from pyspotify.models.albums.requests import RemoveUserSavedAlbumsRequestParams


async def remove_user_saved_albums(
    client: PySpotifyClient, *, album_ids: Sequence[SpotifyItemID]
) -> APICallModel[RemoveUserSavedAlbumsRequest, APIResponse, None]:
    request = RemoveUserSavedAlbumsRequest(
        endpoint="me/albums",
        params=RemoveUserSavedAlbumsRequestParams(
            album_ids=album_ids,
        ),
    )
    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
