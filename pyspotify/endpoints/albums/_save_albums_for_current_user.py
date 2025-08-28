from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import APICallModel
from pyspotify.models.albums.requests import SaveAlbumsForCurrentUserRequest
from pyspotify.models.albums.requests import SaveAlbumsForCurrentUserRequestParams


async def save_albums_for_current_user(
    client: PySpotifyClient, *, album_ids: Sequence[SpotifyItemID]
) -> APICallModel[SaveAlbumsForCurrentUserRequest, APIResponse, None]:
    request = SaveAlbumsForCurrentUserRequest(
        endpoint="me/albums",
        params=SaveAlbumsForCurrentUserRequestParams(
            album_ids=album_ids,
        ),
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
