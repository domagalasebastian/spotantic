from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.artists import get_several_artists
from spotantic.models.artists.requests import GetSeveralArtistsRequest
from spotantic.models.artists.responses import GetSeveralArtistsResponse


@pytest.mark.asyncio
async def test_get_several_artists_builds_request_and_returns_parsed_data():
    client = mock.AsyncMock()
    fake_response = {"artists": []}
    client.request_json.return_value = fake_response

    request_obj = object()
    response_model = SimpleNamespace(artists=[SimpleNamespace(id="a1"), SimpleNamespace(id="a2")])

    with (
        mock.patch.object(GetSeveralArtistsRequest, "build", return_value=request_obj) as build_mock,
        mock.patch.object(GetSeveralArtistsResponse, "model_validate", return_value=response_model) as validate_mock,
    ):
        result = await get_several_artists(client, artist_ids=["a1", "a2"])

        build_mock.assert_called_once_with(artist_ids=["a1", "a2"])
        client.request_json.assert_awaited_once_with(request_obj)
        validate_mock.assert_called_once_with(fake_response)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is response_model.artists
