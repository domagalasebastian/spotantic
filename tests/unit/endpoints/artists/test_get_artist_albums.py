from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.artists import get_artist_albums
from spotantic.models.artists.requests import GetArtistAlbumsRequest
from spotantic.models.spotify import PagedResultModel
from spotantic.models.spotify import SimplifiedAlbumModel
from spotantic.types import AlbumTypes


@pytest.mark.asyncio
async def test_get_artist_albums_builds_request_and_returns_parsed_data():
    client = mock.AsyncMock()
    fake_response = {"items": []}
    client.request_json.return_value = fake_response

    request_obj = object()
    paged = SimpleNamespace(items=[], limit=20, offset=0)

    with (
        mock.patch.object(GetArtistAlbumsRequest, "build", return_value=request_obj) as build_mock,
        mock.patch.object(
            PagedResultModel[SimplifiedAlbumModel], "model_validate", return_value=paged
        ) as validate_mock,
    ):
        result = await get_artist_albums(
            client,
            artist_id="artist123",
            limit=10,
            offset=5,
            market="US",
            include_groups=[AlbumTypes.ALBUM],
        )

        build_mock.assert_called_once_with(
            artist_id="artist123",
            limit=10,
            offset=5,
            market="US",
            include_groups=[AlbumTypes.ALBUM],
        )
        client.request_json.assert_awaited_once_with(request_obj)
        validate_mock.assert_called_once_with(fake_response)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is paged
