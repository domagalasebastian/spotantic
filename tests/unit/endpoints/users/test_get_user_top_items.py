from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.users import get_user_top_items
from spotantic.models.users.requests import GetUserTopItemsRequest
from spotantic.models.users.requests import GetUserTopItemsTimeRange
from spotantic.models.users.requests import GetUserTopItemsType


@pytest.mark.asyncio
async def test_get_user_top_items_artists_builds_request_and_returns_parsed_data():
    client = mock.AsyncMock()
    fake_response = {"items": []}
    client.request_json.return_value = fake_response

    request_obj = object()
    paged_model = SimpleNamespace(items=[])

    with (
        mock.patch.object(GetUserTopItemsRequest, "build", return_value=request_obj) as build_mock,
        mock.patch(
            "spotantic.endpoints.users._get_user_top_items.PagedResultModel",
        ) as paged_mock,
    ):
        paged_mock.return_value.model_validate.return_value = paged_model
        result = await get_user_top_items(
            client,
            item_type=GetUserTopItemsType.ARTISTS,
            time_range=GetUserTopItemsTimeRange.MEDIUM_TERM,
            limit=20,
            offset=0,
        )

        build_mock.assert_called_once_with(
            item_type=GetUserTopItemsType.ARTISTS,
            time_range=GetUserTopItemsTimeRange.MEDIUM_TERM,
            limit=20,
            offset=0,
        )
        client.request_json.assert_awaited_once_with(request_obj)

        assert result.request is request_obj
        assert result.response == fake_response
