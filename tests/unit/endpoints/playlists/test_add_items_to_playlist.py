from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.playlists import add_items_to_playlist
from spotantic.models.playlists.requests import AddItemsToPlaylistRequest


@pytest.mark.asyncio
async def test_add_items_to_playlist_builds_request_and_returns_model():
    client = mock.AsyncMock()
    fake_response = {"snapshot_id": "s1"}
    client.request_json.return_value = fake_response

    request_obj = object()
    fake_model = SimpleNamespace(snapshot_id="s1")

    with mock.patch.object(AddItemsToPlaylistRequest, "build", return_value=request_obj) as build_mock:
        with mock.patch(
            "spotantic.models.playlists.responses.PlaylistSnapshotResponseModel.model_validate", return_value=fake_model
        ) as validate_mock:
            result = await add_items_to_playlist(client, playlist_id="p1", uris=["spotify:track:1"], position=5)

            build_mock.assert_called_once_with(playlist_id="p1", uris=["spotify:track:1"], position=5)
            client.request_json.assert_awaited_once_with(request_obj)
            validate_mock.assert_called_once_with(fake_response)

            assert result.request is request_obj
            assert result.response == fake_response
            assert result.data is fake_model
