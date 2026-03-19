import pytest

from spotantic.endpoints.player import pause_playback
from spotantic.endpoints.player import start_resume_playback
from spotantic.models.player.requests import PausePlaybackRequest
from spotantic.types import SpotifyItemType


@pytest.fixture
async def start_playback(client, example_spotify_uri):
    uri = example_spotify_uri[SpotifyItemType.TRACK]
    await start_resume_playback(client, uris=[uri])


@pytest.mark.asyncio
@pytest.mark.affects_playback
@pytest.mark.requires_active_device
@pytest.mark.usefixtures("start_playback")
async def test_pause_playback(client):
    result = await pause_playback(client)

    assert isinstance(result.request, PausePlaybackRequest)
    assert result.response is None or isinstance(result.response, bytes)
    assert result.data is None
