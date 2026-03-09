from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.episodes import get_user_saved_episodes
from spotantic.models.episodes.requests import GetUserSavedEpisodesRequest
from spotantic.models.spotify import PagedResultModel
from spotantic.models.spotify import SavedEpisodeModel


@pytest.mark.asyncio
async def test_get_user_saved_episodes_builds_request_and_returns_parsed_data():
    client = mock.AsyncMock()
    fake_response = {"items": [], "limit": 20, "offset": 0, "href": "", "total": 0}
    client.request_json.return_value = fake_response

    request_obj = object()
    paged = SimpleNamespace(items=[], limit=20, offset=0)

    with (
        mock.patch.object(GetUserSavedEpisodesRequest, "build", return_value=request_obj) as build_mock,
        mock.patch.object(PagedResultModel[SavedEpisodeModel], "model_validate", return_value=paged) as validate_mock,
    ):
        result = await get_user_saved_episodes(client, limit=10, offset=5, market="US")

        build_mock.assert_called_once_with(limit=10, offset=5, market="US")
        client.request_json.assert_awaited_once_with(request_obj)
        validate_mock.assert_called_once_with(fake_response)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is paged
