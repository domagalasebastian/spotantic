from unittest import mock

import pytest

from spotantic.endpoints.tracks import check_user_saved_tracks
from spotantic.models.tracks.requests import CheckUserSavedTracksRequest


@pytest.mark.asyncio
async def test_check_user_saved_tracks_builds_request_and_returns_mapping():
    client = mock.AsyncMock()
    fake_response = [True, False]
    client.request_json.return_value = fake_response

    request_obj = object()

    with mock.patch.object(CheckUserSavedTracksRequest, "build", return_value=request_obj) as build_mock:
        result = await check_user_saved_tracks(client, track_ids=["t1", "t2"])

        build_mock.assert_called_once_with(track_ids=["t1", "t2"])
        client.request_json.assert_awaited_once_with(request_obj)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data == {"t1": True, "t2": False}
