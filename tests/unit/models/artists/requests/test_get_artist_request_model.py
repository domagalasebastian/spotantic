from http import HTTPMethod

from spotantic.models.artists.requests import GetArtistRequest
from spotantic.models.artists.requests import GetArtistRequestParams
from spotantic.types import SpotifyItemID


def test_get_artist_request(example_instances_of_type):
    artist_id = example_instances_of_type[SpotifyItemID]
    request = GetArtistRequest.build(artist_id=artist_id)

    assert request.endpoint == f"artists/{artist_id}"
    assert request.method_type is HTTPMethod.GET

    params = request.params
    assert isinstance(params, GetArtistRequestParams)
    assert params.artist_id == artist_id
    assert request.body is None

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["id"] == artist_id
