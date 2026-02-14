from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.models import APICallModel
from pyspotify.models.tracks.requests import RemoveUserSavedTracksRequest
from pyspotify.types import APIResponse
from pyspotify.types import SpotifyItemID


async def remove_user_saved_tracks(
    client: PySpotifyClient, *, track_ids: Sequence[SpotifyItemID]
) -> APICallModel[RemoveUserSavedTracksRequest, APIResponse, None]:
    """Remove tracks from the current Spotify user's 'Your Music' library.

    Remove one or more tracks from the current user's 'Your Music' library.

    Args:
        client: PySpotifyClient instance.
        track_ids: A list of the Spotify IDs for the tracks to be removed.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = RemoveUserSavedTracksRequest.build(track_ids=track_ids)
    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
