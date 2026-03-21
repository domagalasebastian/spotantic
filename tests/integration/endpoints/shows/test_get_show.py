import pytest

from spotantic.endpoints.shows import get_show
from spotantic.models.shows.requests import GetShowRequest
from spotantic.models.spotify import ShowModel
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_get_show(client, example_spotify_item_id):
    show_id = example_spotify_item_id[SpotifyItemType.SHOW]
    result = await get_show(client, show_id=show_id)

    assert isinstance(result.request, GetShowRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, ShowModel)
