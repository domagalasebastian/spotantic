import pytest

from spotantic.endpoints.users import get_user_top_items
from spotantic.models.spotify import ArtistModel
from spotantic.models.spotify import PagedResultModel
from spotantic.models.spotify import TrackModel
from spotantic.models.users.requests import GetUserTopItemsRequest
from spotantic.models.users.requests import GetUserTopItemsTimeRange
from spotantic.models.users.requests import GetUserTopItemsType


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_get_user_top_items_tracks(client):
    result = await get_user_top_items(
        client,
        item_type=GetUserTopItemsType.TRACKS,
        time_range=GetUserTopItemsTimeRange.LONG_TERM,
        limit=10,
    )

    assert isinstance(result.request, GetUserTopItemsRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, PagedResultModel)
    assert all(isinstance(item, TrackModel) for item in result.data.items)


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_get_user_top_items_artists(client):
    result = await get_user_top_items(
        client,
        item_type=GetUserTopItemsType.ARTISTS,
        time_range=GetUserTopItemsTimeRange.SHORT_TERM,
        limit=50,
    )

    assert isinstance(result.request, GetUserTopItemsRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, PagedResultModel)
    assert all(isinstance(item, ArtistModel) for item in result.data.items)
