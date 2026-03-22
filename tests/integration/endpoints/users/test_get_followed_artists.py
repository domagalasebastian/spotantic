import pytest

from spotantic.endpoints.users import get_followed_artists
from spotantic.models.spotify import ArtistModel
from spotantic.models.spotify import PagedResultWithCursorsModel
from spotantic.models.users.requests import GetFollowedArtistsRequest


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_get_followed_artists(client):
    result = await get_followed_artists(client, limit=50)

    assert isinstance(result.request, GetFollowedArtistsRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, PagedResultWithCursorsModel)
    assert all(isinstance(item, ArtistModel) for item in result.data.items)
