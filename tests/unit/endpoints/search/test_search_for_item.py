from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.search import search_for_item
from spotantic.models.search.requests import SearchForItemIncludeExternal
from spotantic.models.search.requests import SearchForItemRequest
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
async def test_search_for_item_builds_request_and_returns_model() -> None:
    client = mock.AsyncMock()
    fake_response = {"tracks": {}}
    client.request_json.return_value = fake_response

    request_obj = object()
    fake_model = SimpleNamespace(tracks={})

    with mock.patch.object(SearchForItemRequest, "build", return_value=request_obj) as build_mock:
        with mock.patch(
            "spotantic.models.search.responses.SearchForItemResponse.model_validate",
            return_value=fake_model,
        ) as validate_mock:
            result = await search_for_item(
                client,
                query="test",
                item_type=[SpotifyItemType.TRACK],
                market="US",
                limit=5,
                offset=0,
                include_external=SearchForItemIncludeExternal.AUDIO,
            )

            build_mock.assert_called_once_with(
                query="test",
                item_type=[SpotifyItemType.TRACK],
                market="US",
                limit=5,
                offset=0,
                include_external=SearchForItemIncludeExternal.AUDIO,
            )
            client.request_json.assert_awaited_once_with(request_obj)
            validate_mock.assert_called_once_with(fake_response)

            assert result.request is request_obj
            assert result.response == fake_response
            assert result.data is fake_model
