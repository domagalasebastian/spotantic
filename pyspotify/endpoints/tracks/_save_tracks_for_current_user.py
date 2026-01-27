from datetime import datetime
from typing import Optional
from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import APICallModel
from pyspotify.models.tracks.requests import SaveTracksForCurrentUserRequest


async def save_tracks_for_current_user(
    client: PySpotifyClient,
    *,
    track_ids: Optional[Sequence[SpotifyItemID]] = None,
    timestamped_track_ids: Optional[dict[SpotifyItemID, datetime]] = None,
) -> APICallModel[SaveTracksForCurrentUserRequest, APIResponse, None]:
    """Save tracks to the current Spotify user's 'Your Music' library.

    Save one or more tracks to the current user's 'Your Music' library.

    Args:
        client: PySpotifyClient instance.
        track_ids: A list of the Spotify IDs for the tracks to be saved.
        timestamped_track_ids: A dictionary mapping Spotify track IDs to the datetime they were added.
          This allows you to specify when tracks were added to maintain a specific chronological order
          in the user's library.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = SaveTracksForCurrentUserRequest.build(track_ids=track_ids, timestamped_ids=timestamped_track_ids)
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
