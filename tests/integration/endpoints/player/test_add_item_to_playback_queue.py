import pytest

from spotantic.endpoints.player import add_item_to_playback_queue
from spotantic.models.player.requests import AddItemToPlaybackQueueRequest
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.affects_playback
@pytest.mark.requires_active_device
async def test_add_item_to_playback_queue(client, example_spotify_uri):
    track_uri = example_spotify_uri[SpotifyItemType.TRACK]

    result = await add_item_to_playback_queue(client, uri=track_uri)

    assert isinstance(result.request, AddItemToPlaybackQueueRequest)
    assert result.response is None or isinstance(result.response, bytes)
    assert result.data is None
