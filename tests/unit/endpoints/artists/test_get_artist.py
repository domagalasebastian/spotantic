from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.artists import get_artist
from spotantic.models.artists.requests import GetArtistRequest
from spotantic.models.spotify import ArtistModel


@pytest.mark.asyncio
async def test_get_artist_builds_request_and_returns_parsed_data():
    client = mock.AsyncMock()
    fake_response = {"id": "artist123"}
    client.request_json.return_value = fake_response

    request_obj = object()
    artist_model = SimpleNamespace(id="artist123")

    with (
        mock.patch.object(GetArtistRequest, "build", return_value=request_obj) as build_mock,
        mock.patch.object(ArtistModel, "model_validate", return_value=artist_model) as validate_mock,
    ):
        result = await get_artist(client, artist_id="artist123")

        build_mock.assert_called_once_with(artist_id="artist123")
        client.request_json.assert_awaited_once_with(request_obj)
        validate_mock.assert_called_once_with(fake_response)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is artist_model
