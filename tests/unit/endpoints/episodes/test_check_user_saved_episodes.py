from unittest import mock

import pytest

from spotantic.endpoints.episodes import check_user_saved_episodes
from spotantic.models.episodes.requests import CheckUserSavedEpisodesRequest


@pytest.mark.asyncio
async def test_check_user_saved_episodes_builds_request_and_returns_mapping():
    client = mock.AsyncMock()
    fake_response = [True, False]
    client.request_json.return_value = fake_response

    request_obj = object()

    with mock.patch.object(CheckUserSavedEpisodesRequest, "build", return_value=request_obj) as build_mock:
        result = await check_user_saved_episodes(client, episode_ids=["e1", "e2"])

        build_mock.assert_called_once_with(episode_ids=["e1", "e2"])
        client.request_json.assert_awaited_once_with(request_obj)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data == {"e1": True, "e2": False}
