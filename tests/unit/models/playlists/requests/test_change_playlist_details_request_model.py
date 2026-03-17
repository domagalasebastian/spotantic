from http import HTTPMethod

from spotantic.models.playlists.requests import ChangePlaylistDetailsRequest
from spotantic.models.playlists.requests import ChangePlaylistDetailsRequestBody
from spotantic.models.playlists.requests import ChangePlaylistDetailsRequestParams
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID


def test_change_playlist_details_request_model_serializes_body_and_params(example_instances_of_type) -> None:
    example_id = example_instances_of_type[SpotifyItemID]

    req = ChangePlaylistDetailsRequest.build(
        playlist_id=example_id,
        name="New name",
        public=True,
        collaborative=False,
        description="desc",
    )

    assert req.endpoint == f"playlists/{example_id}"
    assert req.method_type is HTTPMethod.PUT
    assert req.headers.content_type == "application/json"
    assert AuthScope.PLAYLIST_MODIFY_PRIVATE in req.required_scopes
    assert AuthScope.PLAYLIST_MODIFY_PUBLIC in req.required_scopes

    body = req.body
    assert isinstance(body, ChangePlaylistDetailsRequestBody)
    assert body.name == "New name"
    assert body.public is True
    assert body.collaborative is False
    assert body.description == "desc"

    params = req.params
    assert isinstance(params, ChangePlaylistDetailsRequestParams)
    assert params.playlist_id == example_id
