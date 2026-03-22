import pytest

from spotantic.endpoints.tracks import check_user_saved_tracks
from spotantic.models.tracks.requests import CheckUserSavedTracksRequest
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.readonly
@pytest.mark.user_library
async def test_check_user_saved_tracks(client, example_spotify_item_id):
    track_id = example_spotify_item_id[SpotifyItemType.TRACK]

    result = await check_user_saved_tracks(client, track_ids=[track_id])

    assert isinstance(result.request, CheckUserSavedTracksRequest)
    assert isinstance(result.response, list)
    assert isinstance(result.data, dict)
    assert len(result.data) == 1
    assert isinstance(result.data[track_id], bool)
