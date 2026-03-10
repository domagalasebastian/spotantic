from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.player import get_currently_playing_track
from spotantic.models.player.requests import GetCurrentlyPlayingTrackRequest
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
async def test_get_currently_playing_track_builds_request_and_returns_model():
    client = mock.AsyncMock()
    fake_response = {"dummy": "value"}
    client.request_json.return_value = fake_response

    request_obj = object()
    fake_model = SimpleNamespace(dummy="value")

    with mock.patch.object(GetCurrentlyPlayingTrackRequest, "build", return_value=request_obj) as build_mock:
        with mock.patch(
            "spotantic.models.spotify.CurrentlyPlayingItemModel.model_validate", return_value=fake_model
        ) as validate_mock:
            result = await get_currently_playing_track(client, additional_types=[SpotifyItemType.TRACK], market="US")

            build_mock.assert_called_once_with(additional_types=[SpotifyItemType.TRACK], market="US")
            client.request_json.assert_awaited_once_with(request_obj)
            validate_mock.assert_called_once_with(fake_response)

            assert result.request is request_obj
            assert result.response == fake_response
            assert result.data is fake_model
