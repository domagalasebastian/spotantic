from unittest import mock

import pytest

from spotantic.endpoints.shows import check_user_saved_shows
from spotantic.models.shows.requests import CheckUserSavedShowsRequest


@pytest.mark.asyncio
async def test_check_user_saved_shows_builds_request_and_returns_mapping():
    client = mock.AsyncMock()
    fake_response = [True, False]
    client.request_json.return_value = fake_response

    request_obj = object()

    with mock.patch.object(CheckUserSavedShowsRequest, "build", return_value=request_obj) as build_mock:
        result = await check_user_saved_shows(client, show_ids=["s1", "s2"])

        build_mock.assert_called_once_with(show_ids=["s1", "s2"])
        client.request_json.assert_awaited_once_with(request_obj)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data == {"s1": True, "s2": False}
