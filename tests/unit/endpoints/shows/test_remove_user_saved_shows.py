from unittest import mock

import pytest

from spotantic.endpoints.shows import remove_user_saved_shows
from spotantic.models.shows.requests import RemoveUserSavedShowsRequest


@pytest.mark.asyncio
async def test_remove_user_saved_shows_builds_request_and_returns_none_data():
    client = mock.AsyncMock()
    fake_response = None
    client.request.return_value = fake_response

    request_obj = object()

    with mock.patch.object(RemoveUserSavedShowsRequest, "build", return_value=request_obj) as build_mock:
        result = await remove_user_saved_shows(client, show_ids=["s1", "s2"], market="US")

        build_mock.assert_called_once_with(show_ids=["s1", "s2"], market="US")
        client.request.assert_awaited_once_with(request_obj)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is None
