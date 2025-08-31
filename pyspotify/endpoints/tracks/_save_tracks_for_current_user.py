from datetime import datetime
from typing import Dict
from typing import Optional
from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import APICallModel
from pyspotify.models.tracks.requests import SaveTracksForCurrentUserRequest
from pyspotify.models.tracks.requests import SaveTracksForCurrentUserRequestBody
from pyspotify.models.tracks.requests._save_tracks_for_current_user import TimestampTrackIDModel


async def save_tracks_for_current_user(
    client: PySpotifyClient,
    *,
    track_ids: Optional[Sequence[SpotifyItemID]] = None,
    timestamped_track_ids: Optional[Dict[SpotifyItemID, datetime]] = None,
) -> APICallModel[SaveTracksForCurrentUserRequest, APIResponse, None]:
    timestamped_ids = None
    if timestamped_track_ids is not None:
        timestamped_ids = []
        for track_id, timestamp in timestamped_track_ids.items():
            timestamped_ids.append(TimestampTrackIDModel(track_id=track_id, added_at=timestamp))

    request = SaveTracksForCurrentUserRequest(
        endpoint="me/tracks",
        body=SaveTracksForCurrentUserRequestBody(
            track_ids=track_ids,
            timestamped_ids=timestamped_ids,
        ),
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
