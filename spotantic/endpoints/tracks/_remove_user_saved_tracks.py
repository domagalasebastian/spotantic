from typing import Sequence

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.tracks.requests import RemoveUserSavedTracksRequest
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemID


async def remove_user_saved_tracks(
    client: SpotanticClient, *, track_ids: Sequence[SpotifyItemID]
) -> APICallModel[RemoveUserSavedTracksRequest, APIResponse, None]:
    """Remove tracks from the current Spotify user's 'Your Music' library.

    Remove one or more tracks from the current user's 'Your Music' library.

    Args:
        client: SpotanticClient instance.
        track_ids: A list of the Spotify IDs for the tracks to be removed.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = RemoveUserSavedTracksRequest.build(track_ids=track_ids)
    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
