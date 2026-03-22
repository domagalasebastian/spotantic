import pytest

from spotantic.endpoints.tracks import check_user_saved_tracks
from spotantic.endpoints.tracks import remove_user_saved_tracks
from spotantic.endpoints.tracks import save_tracks_for_current_user
from spotantic.models.tracks.requests import RemoveUserSavedTracksRequest
from spotantic.types import SpotifyItemType


@pytest.fixture
async def track_id(client, example_spotify_item_id):
    track_id = example_spotify_item_id[SpotifyItemType.TRACK]
    data = await check_user_saved_tracks(client, track_ids=[track_id])
    is_present_in_library = data.data[track_id]

    yield track_id

    if is_present_in_library:
        await save_tracks_for_current_user(client, track_ids=[track_id])


@pytest.mark.asyncio
@pytest.mark.mutation
@pytest.mark.user_library
async def test_remove_user_saved_tracks(client, track_id):
    result = await remove_user_saved_tracks(client, track_ids=[track_id])

    assert isinstance(result.request, RemoveUserSavedTracksRequest)
    assert result.response is None or isinstance(result.response, bytes)
    assert result.data is None
