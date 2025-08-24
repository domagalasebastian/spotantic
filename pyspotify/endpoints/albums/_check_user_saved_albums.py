from typing import Dict
from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models._api_call_model import APICallModel
from pyspotify.models.albums.requests import CheckUserSavedAlbumsRequest
from pyspotify.models.albums.requests import CheckUserSavedAlbumsRequestParams


async def check_user_saved_albums(
    client: PySpotifyClient, *, album_ids: Sequence[SpotifyItemID]
) -> APICallModel[CheckUserSavedAlbumsRequest, APIResponse, Dict[SpotifyItemID, bool]]:
    request = CheckUserSavedAlbumsRequest(
        endpoint="me/albums/contains",
        params=CheckUserSavedAlbumsRequestParams(
            album_ids=album_ids,
        ),
    )
    response = await client.request(request)
    assert response is not None
    data = dict(zip(album_ids, response))

    return APICallModel(request=request, response=response, data=data)
