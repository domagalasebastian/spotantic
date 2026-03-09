from unittest import mock

import pytest

from spotantic.endpoints.library import remove_items_from_library
from spotantic.models.library.requests import RemoveItemsFromLibraryRequest


@pytest.mark.asyncio
async def test_remove_items_from_library_builds_request_and_returns_none_data():
    client = mock.AsyncMock()
    fake_response = None
    client.request.return_value = fake_response

    request_obj = object()

    with mock.patch.object(RemoveItemsFromLibraryRequest, "build", return_value=request_obj) as build_mock:
        result = await remove_items_from_library(client, uris=["spotify:track:1", "spotify:album:2"])

        build_mock.assert_called_once_with(uris=["spotify:track:1", "spotify:album:2"])
        client.request.assert_awaited_once_with(request_obj)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is None
