from unittest import mock

import pytest

from spotantic.endpoints.episodes import save_episodes_for_current_user
from spotantic.models.episodes.requests import SaveEpisodesForCurrentUserRequest


@pytest.mark.asyncio
async def test_save_episodes_for_current_user_builds_request_and_returns_none_data():
    client = mock.AsyncMock()
    fake_response = None
    client.request.return_value = fake_response

    request_obj = object()

    with mock.patch.object(SaveEpisodesForCurrentUserRequest, "build", return_value=request_obj) as build_mock:
        result = await save_episodes_for_current_user(client, episode_ids=["e1", "e2"])

        build_mock.assert_called_once_with(episode_ids=["e1", "e2"])
        client.request.assert_awaited_once_with(request_obj)

        assert result.request is request_obj
        assert result.response is fake_response
        assert result.data is None
