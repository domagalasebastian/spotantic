from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.shows import get_show_episodes
from spotantic.models.shows.requests import GetShowEpisodesRequest
from spotantic.models.spotify import PagedResultModel
from spotantic.models.spotify import SimplifiedEpisodeModel


@pytest.mark.asyncio
async def test_get_show_episodes_builds_request_and_returns_parsed_data():
    client = mock.AsyncMock()
    fake_response = {"items": [], "limit": 10, "offset": 0, "href": "", "total": 0}
    client.request_json.return_value = fake_response

    request_obj = object()
    paged = SimpleNamespace(items=[], limit=10, offset=0)

    with (
        mock.patch.object(GetShowEpisodesRequest, "build", return_value=request_obj) as build_mock,
        mock.patch.object(
            PagedResultModel[SimplifiedEpisodeModel], "model_validate", return_value=paged
        ) as validate_mock,
    ):
        result = await get_show_episodes(client, show_id="s1", limit=5, offset=3, market="US")

        build_mock.assert_called_once_with(show_id="s1", limit=5, offset=3, market="US")
        client.request_json.assert_awaited_once_with(request_obj)
        validate_mock.assert_called_once_with(fake_response)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is paged
