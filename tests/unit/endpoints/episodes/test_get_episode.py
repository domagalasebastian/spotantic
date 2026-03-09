from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.episodes import get_episode
from spotantic.models.episodes.requests import GetEpisodeRequest
from spotantic.models.spotify import EpisodeModel


@pytest.mark.asyncio
async def test_get_episode_builds_request_and_returns_parsed_data():
    client = mock.AsyncMock()
    fake_response = {"id": "ep123"}
    client.request_json.return_value = fake_response

    request_obj = object()
    episode_model = SimpleNamespace(id="ep123")

    with (
        mock.patch.object(GetEpisodeRequest, "build", return_value=request_obj) as build_mock,
        mock.patch.object(EpisodeModel, "model_validate", return_value=episode_model) as validate_mock,
    ):
        result = await get_episode(client, episode_id="ep123", market="US")

        build_mock.assert_called_once_with(episode_id="ep123", market="US")
        client.request_json.assert_awaited_once_with(request_obj)
        validate_mock.assert_called_once_with(fake_response)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is episode_model
