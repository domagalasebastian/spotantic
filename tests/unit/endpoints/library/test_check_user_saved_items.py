from unittest import mock

import pytest
from pydantic import ValidationError

from spotantic.endpoints.library import check_user_saved_items
from spotantic.models.library.requests import CheckUserSavedItemsRequest


@pytest.mark.asyncio
async def test_check_user_saved_items_builds_request_and_returns_mapping():
    client = mock.AsyncMock()
    fake_response = [True, False]
    client.request_json.return_value = fake_response

    request_obj = object()

    with mock.patch.object(CheckUserSavedItemsRequest, "build", return_value=request_obj) as build_mock:
        result = await check_user_saved_items(client, uris=["spotify:track:1", "spotify:album:2"])

        build_mock.assert_called_once_with(uris=["spotify:track:1", "spotify:album:2"])
        client.request_json.assert_awaited_once_with(request_obj)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data == {"spotify:track:1": True, "spotify:album:2": False}


@pytest.mark.asyncio
async def test_check_user_saved_items_raises_on_invalid_response_type():
    client = mock.AsyncMock()
    # Response must be a list[bool]; dict is invalid and should raise a ValidationError
    client.request_json.return_value = {"spotify:track:1": True}

    request_obj = object()

    with mock.patch.object(CheckUserSavedItemsRequest, "build", return_value=request_obj):
        with pytest.raises(ValidationError):
            await check_user_saved_items(client, uris=["spotify:track:1"])
