import pytest

from spotantic.endpoints.shows import get_several_shows
from spotantic.models.shows.requests import GetSeveralShowsRequest
from spotantic.models.spotify import SimplifiedShowModel
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_get_several_shows(client, example_spotify_item_id):
    show_id = example_spotify_item_id[SpotifyItemType.SHOW]
    result = await get_several_shows(client, show_ids=[show_id])

    assert isinstance(result.request, GetSeveralShowsRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, list)
    assert len(result.data) == 1
    assert isinstance(result.data[0], SimplifiedShowModel)
