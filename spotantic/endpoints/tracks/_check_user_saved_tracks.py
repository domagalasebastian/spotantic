from typing import Sequence

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.tracks.requests import CheckUserSavedTracksRequest
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemID


async def check_user_saved_tracks(
    client: SpotanticClient, *, track_ids: Sequence[SpotifyItemID]
) -> APICallModel[CheckUserSavedTracksRequest, APIResponse, dict[SpotifyItemID, bool]]:
    """Check if tracks are saved in the current Spotify user's 'Your Music' library.

    Check if one or more tracks is already saved in the current Spotify user's 'Your Music' library.

    Args:
        client: SpotanticClient instance.
        track_ids: A list of the Spotify IDs for the tracks.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = CheckUserSavedTracksRequest.build(track_ids=track_ids)
    response = await client.request(request)
    assert response is not None
    data = dict(zip(track_ids, response))

    return APICallModel(request=request, response=response, data=data)
