from http import HTTPMethod

from spotantic.models.artists.requests import GetSeveralArtistsRequest
from spotantic.models.artists.requests import GetSeveralArtistsRequestParams
from spotantic.types import SpotifyItemID
from tests.unit._helpers import _example_instances_of_type


def test_get_several_artists_request():
    artist_id = _example_instances_of_type[SpotifyItemID]
    artist_ids = [artist_id, artist_id]
    request = GetSeveralArtistsRequest.build(artist_ids=artist_ids)

    assert request.endpoint == "artists"
    assert request.method_type is HTTPMethod.GET

    params = request.params
    assert isinstance(params, GetSeveralArtistsRequestParams)
    assert params.artist_ids == artist_ids
    assert request.body is None

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["ids"] == ",".join(artist_ids)
