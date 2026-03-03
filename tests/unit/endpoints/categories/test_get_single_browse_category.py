from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.categories import get_single_browse_category
from spotantic.models.categories.requests import GetSingleBrowseCategoryRequest
from spotantic.models.spotify import CategoryModel


@pytest.mark.asyncio
async def test_get_single_browse_category_builds_request_and_returns_parsed_data():
    client = mock.AsyncMock()
    fake_response = {"id": "cat123"}
    client.request_json.return_value = fake_response

    request_obj = object()
    category_model = SimpleNamespace(category_id="cat123")

    with (
        mock.patch.object(GetSingleBrowseCategoryRequest, "build", return_value=request_obj) as build_mock,
        mock.patch.object(CategoryModel, "model_validate", return_value=category_model) as validate_mock,
    ):
        result = await get_single_browse_category(client, category_id="cat123", locale="en_US")

        build_mock.assert_called_once_with(category_id="cat123", locale="en_US")
        client.request_json.assert_awaited_once_with(request_obj)
        validate_mock.assert_called_once_with(fake_response)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is category_model
