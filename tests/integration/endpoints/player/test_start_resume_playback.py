import pytest

from spotantic.endpoints.player import start_resume_playback
from spotantic.models.player.requests import StartResumePlaybackRequest
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.affects_playback
@pytest.mark.requires_active_device
async def test_start_resume_playback(client, example_spotify_uri):
    album_uri = example_spotify_uri[SpotifyItemType.ALBUM]
    track_uri = example_spotify_uri[SpotifyItemType.TRACK]

    result = await start_resume_playback(client, context_uri=album_uri, offset=track_uri, position_ms=60000)

    assert isinstance(result.request, StartResumePlaybackRequest)
    assert result.response is None or isinstance(result.response, bytes)
    assert result.data is None
