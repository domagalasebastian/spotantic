from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.categories import get_several_browse_categories
from spotantic.models.categories.requests import GetSeveralBrowseCategoriesRequest
from spotantic.models.categories.responses import GetSeveralBrowseCategoriesResponse


@pytest.mark.asyncio
async def test_get_several_browse_categories_builds_request_and_returns_parsed_data():
    client = mock.AsyncMock()
    fake_response = {"categories": {"items": []}}
    client.request_json.return_value = fake_response

    request_obj = object()
    container = SimpleNamespace(categories=SimpleNamespace(items=[], limit=20, offset=0))

    with (
        mock.patch.object(GetSeveralBrowseCategoriesRequest, "build", return_value=request_obj) as build_mock,
        mock.patch.object(
            GetSeveralBrowseCategoriesResponse, "model_validate", return_value=container
        ) as validate_mock,
    ):
        result = await get_several_browse_categories(client, limit=5, offset=1, locale="en_US")

        build_mock.assert_called_once_with(limit=5, offset=1, locale="en_US")
        client.request_json.assert_awaited_once_with(request_obj)
        validate_mock.assert_called_once_with(fake_response)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is container.categories
