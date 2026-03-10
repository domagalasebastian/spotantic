from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.player import get_recently_played_tracks
from spotantic.models.player.requests import GetRecentlyPlayedTracksRequest


@pytest.mark.asyncio
async def test_get_recently_played_tracks_builds_request_and_returns_model():
    client = mock.AsyncMock()
    fake_response = {"dummy": "value"}
    client.request_json.return_value = fake_response

    request_obj = object()
    fake_model = SimpleNamespace(dummy="value")

    with mock.patch.object(GetRecentlyPlayedTracksRequest, "build", return_value=request_obj) as build_mock:
        with mock.patch(
            "spotantic.models.spotify.PagedResultWithCursorsModel.model_validate", return_value=fake_model
        ) as validate_mock:
            result = await get_recently_played_tracks(client, limit=10, after=123)

            build_mock.assert_called_once_with(limit=10, after=123, before=None)
            client.request_json.assert_awaited_once_with(request_obj)
            validate_mock.assert_called_once_with(fake_response)

            assert result.request is request_obj
            assert result.response == fake_response
            assert result.data is fake_model
