from typing import Dict
from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import APICallModel
from pyspotify.models.tracks.requests import CheckUserSavedTracksRequest
from pyspotify.models.tracks.requests import CheckUserSavedTracksRequestParams


async def check_user_saved_tracks(
    client: PySpotifyClient, *, track_ids: Sequence[SpotifyItemID]
) -> APICallModel[CheckUserSavedTracksRequest, APIResponse, Dict[SpotifyItemID, bool]]:
    request = CheckUserSavedTracksRequest(
        endpoint="me/tracks/contains",
        params=CheckUserSavedTracksRequestParams(
            track_ids=track_ids,
        ),
    )
    response = await client.request(request)
    assert response is not None
    data = dict(zip(track_ids, response))

    return APICallModel(request=request, response=response, data=data)
