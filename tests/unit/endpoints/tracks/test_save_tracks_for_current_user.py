from unittest import mock

import pytest

from spotantic.endpoints.tracks import save_tracks_for_current_user
from spotantic.models.tracks.requests import SaveTracksForCurrentUserRequest


@pytest.mark.asyncio
async def test_save_tracks_for_current_user_builds_request_and_returns_none_data():
    client = mock.AsyncMock()
    fake_response = None
    client.request.return_value = fake_response

    request_obj = object()

    with mock.patch.object(SaveTracksForCurrentUserRequest, "build", return_value=request_obj) as build_mock:
        result = await save_tracks_for_current_user(client, track_ids=["t1", "t2"])

        build_mock.assert_called_once_with(track_ids=["t1", "t2"], timestamped_ids=None)
        client.request.assert_awaited_once_with(request_obj)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is None
