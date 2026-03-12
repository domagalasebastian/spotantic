from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.tracks import get_track
from spotantic.models.spotify import TrackModel
from spotantic.models.tracks.requests import GetTrackRequest


@pytest.mark.asyncio
async def test_get_track_builds_request_and_returns_parsed_data():
    client = mock.AsyncMock()
    fake_response = {"id": "track123"}
    client.request_json.return_value = fake_response

    request_obj = object()
    track_model = SimpleNamespace(id="track123")

    with (
        mock.patch.object(GetTrackRequest, "build", return_value=request_obj) as build_mock,
        mock.patch.object(TrackModel, "model_validate", return_value=track_model) as validate_mock,
    ):
        result = await get_track(client, track_id="track123", market="US")

        build_mock.assert_called_once_with(track_id="track123", market="US")
        client.request_json.assert_awaited_once_with(request_obj)
        validate_mock.assert_called_once_with(fake_response)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is track_model
