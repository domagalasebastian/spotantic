from http import HTTPMethod

from spotantic.models.users.requests import FollowPlaylistRequest
from spotantic.models.users.requests import FollowPlaylistRequestBody
from spotantic.models.users.requests import FollowPlaylistRequestParams
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID


def test_follow_playlist_request(example_instances_of_type):
    playlist_id = example_instances_of_type[SpotifyItemID]
    request = FollowPlaylistRequest.build(playlist_id=playlist_id, public=True)

    assert request.endpoint == f"playlists/{playlist_id}/followers"
    assert request.method_type is HTTPMethod.PUT
    assert AuthScope.PLAYLIST_MODIFY_PRIVATE in request.required_scopes
    assert AuthScope.PLAYLIST_MODIFY_PUBLIC in request.required_scopes

    params = request.params
    assert isinstance(params, FollowPlaylistRequestParams)
    assert params.playlist_id == playlist_id

    body = request.body
    assert isinstance(body, FollowPlaylistRequestBody)
    assert body.public is True
