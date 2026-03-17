from http import HTTPMethod

from spotantic.models.playlists.requests import GetPlaylistCoverImageRequest
from spotantic.models.playlists.requests import GetPlaylistCoverImageRequestParams
from spotantic.types import SpotifyItemID


def test_get_playlist_cover_image_request_model(example_instances_of_type):
    example_id = example_instances_of_type[SpotifyItemID]
    req = GetPlaylistCoverImageRequest.build(playlist_id=example_id)

    assert req.endpoint == f"playlists/{example_id}/images"
    assert req.method_type is HTTPMethod.GET
    params = req.params
    assert isinstance(params, GetPlaylistCoverImageRequestParams)
    assert params.playlist_id == example_id
    assert req.body is None

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["id"] == example_id
