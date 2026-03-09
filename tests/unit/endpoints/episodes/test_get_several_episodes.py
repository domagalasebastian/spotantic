from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.episodes import get_several_episodes
from spotantic.models.episodes.requests import GetSeveralEpisodesRequest
from spotantic.models.episodes.responses import GetSeveralEpisodesResponse


@pytest.mark.asyncio
async def test_get_several_episodes_builds_request_and_returns_parsed_data():
    client = mock.AsyncMock()
    fake_response = {"episodes": []}
    client.request_json.return_value = fake_response

    request_obj = object()
    response_model = SimpleNamespace(episodes=[SimpleNamespace(id="e1")])

    with (
        mock.patch.object(GetSeveralEpisodesRequest, "build", return_value=request_obj) as build_mock,
        mock.patch.object(GetSeveralEpisodesResponse, "model_validate", return_value=response_model) as validate_mock,
    ):
        result = await get_several_episodes(client, episode_ids=["e1"], market="US")

        build_mock.assert_called_once_with(episode_ids=["e1"], market="US")
        client.request_json.assert_awaited_once_with(request_obj)
        validate_mock.assert_called_once_with(fake_response)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is response_model.episodes
