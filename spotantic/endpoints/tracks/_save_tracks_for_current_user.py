from datetime import datetime
from typing import Optional
from typing import Sequence

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.tracks.requests import SaveTracksForCurrentUserRequest
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemID


async def save_tracks_for_current_user(
    client: SpotanticClient,
    *,
    track_ids: Optional[Sequence[SpotifyItemID]] = None,
    timestamped_track_ids: Optional[dict[SpotifyItemID, datetime]] = None,
) -> APICallModel[SaveTracksForCurrentUserRequest, APIResponse, None]:
    """Save tracks to the current Spotify user's 'Your Music' library.

    Save one or more tracks to the current user's 'Your Music' library.

    Args:
        client: SpotanticClient instance.
        track_ids: A list of the Spotify IDs for the tracks to be saved.
        timestamped_track_ids: A dictionary mapping Spotify track IDs to the datetime they were added.
          This allows you to specify when tracks were added to maintain a specific chronological order
          in the user's library.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = SaveTracksForCurrentUserRequest.build(track_ids=track_ids, timestamped_ids=timestamped_track_ids)
    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
