from unittest import mock

import pytest

from spotantic.endpoints.shows import save_shows_for_current_user
from spotantic.models.shows.requests import SaveShowsForCurrentUserRequest


@pytest.mark.asyncio
async def test_save_shows_for_current_user_builds_request_and_returns_none_data():
    client = mock.AsyncMock()
    fake_response = None
    client.request.return_value = fake_response

    request_obj = object()

    with mock.patch.object(SaveShowsForCurrentUserRequest, "build", return_value=request_obj) as build_mock:
        result = await save_shows_for_current_user(client, show_ids=["s1", "s2"])

        build_mock.assert_called_once_with(show_ids=["s1", "s2"])
        client.request.assert_awaited_once_with(request_obj)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is None
