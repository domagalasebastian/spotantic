from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.artists import get_artist_top_tracks
from spotantic.models.artists.requests import GetArtistTopTracksRequest
from spotantic.models.artists.responses import GetArtistTopTracksResponse


@pytest.mark.asyncio
async def test_get_artist_top_tracks_builds_request_and_returns_parsed_data():
    client = mock.AsyncMock()
    fake_response = {"tracks": []}
    client.request_json.return_value = fake_response

    request_obj = object()
    response_model = SimpleNamespace(tracks=[SimpleNamespace(id="t1"), SimpleNamespace(id="t2")])

    with (
        mock.patch.object(GetArtistTopTracksRequest, "build", return_value=request_obj) as build_mock,
        mock.patch.object(GetArtistTopTracksResponse, "model_validate", return_value=response_model) as validate_mock,
    ):
        result = await get_artist_top_tracks(client, artist_id="artist123", market="US")

        build_mock.assert_called_once_with(artist_id="artist123", market="US")
        client.request_json.assert_awaited_once_with(request_obj)
        validate_mock.assert_called_once_with(fake_response)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is response_model.tracks
