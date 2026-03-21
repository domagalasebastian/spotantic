import pytest

from spotantic.endpoints.playlists import change_playlist_details
from spotantic.models.playlists.requests import ChangePlaylistDetailsRequest


@pytest.mark.asyncio
@pytest.mark.mutation
async def test_change_playlist_details(client, playlist_data):
    result = await change_playlist_details(
        client,
        playlist_id=playlist_data.playlist_id,
        name="Updated Name",
        description="Updated Description",
    )

    assert isinstance(result.request, ChangePlaylistDetailsRequest)
    assert result.response is None or isinstance(result.response, bytes)
    assert result.data is None
