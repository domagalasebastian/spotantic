from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.users import get_followed_artists
from spotantic.models.users.requests import GetFollowedArtistsRequest
from spotantic.models.users.responses import GetFollowedArtistsResponse
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
async def test_get_followed_artists_builds_request_and_returns_parsed_data():
    client = mock.AsyncMock()
    fake_response = {"artists": []}
    client.request_json.return_value = fake_response

    request_obj = object()
    response_model = SimpleNamespace(artists=[SimpleNamespace(id="a1")])

    with (
        mock.patch.object(GetFollowedArtistsRequest, "build", return_value=request_obj) as build_mock,
        mock.patch.object(GetFollowedArtistsResponse, "model_validate", return_value=response_model) as validate_mock,
    ):
        result = await get_followed_artists(client, item_type=SpotifyItemType.ARTIST, after=None, limit=20)

        build_mock.assert_called_once_with(
            item_type=SpotifyItemType.ARTIST,
            after=None,
            limit=20,
        )
        client.request_json.assert_awaited_once_with(request_obj)
        validate_mock.assert_called_once_with(fake_response)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is response_model.artists
