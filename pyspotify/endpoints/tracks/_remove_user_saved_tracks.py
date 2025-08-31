from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import APICallModel
from pyspotify.models.tracks.requests import RemoveUserSavedTracksRequest
from pyspotify.models.tracks.requests import RemoveUserSavedTracksRequestParams


async def remove_user_saved_tracks(
    client: PySpotifyClient, *, track_ids: Sequence[SpotifyItemID]
) -> APICallModel[RemoveUserSavedTracksRequest, APIResponse, None]:
    request = RemoveUserSavedTracksRequest(
        endpoint="me/tracks",
        params=RemoveUserSavedTracksRequestParams(
            track_ids=track_ids,
        ),
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
