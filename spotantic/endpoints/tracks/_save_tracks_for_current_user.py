from collections.abc import Sequence
from datetime import datetime
from typing import Optional

from typing_extensions import deprecated

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.tracks.requests import SaveTracksForCurrentUserRequest
from spotantic.types import RawAPIResponse
from spotantic.types import SpotifyItemID


@deprecated("This endpoint is deprecated. Use Save Items to Library instead.")
async def save_tracks_for_current_user(
    client: SpotanticClient,
    *,
    track_ids: Optional[Sequence[SpotifyItemID]] = None,
    timestamped_track_ids: Optional[dict[SpotifyItemID, datetime]] = None,
) -> APICallModel[SaveTracksForCurrentUserRequest, RawAPIResponse, None]:
    """Save one or more tracks to the current user's 'Your Music' library.

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users (March 9 2026 for old users).
       Use *Save Items to Library* instead.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
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
