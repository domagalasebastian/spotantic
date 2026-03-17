from http import HTTPMethod

from spotantic.models.users.requests import UnfollowPlaylistRequest
from spotantic.models.users.requests import UnfollowPlaylistRequestParams
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID


def test_unfollow_playlist_request(example_instances_of_type):
    playlist_id = example_instances_of_type[SpotifyItemID]
    request = UnfollowPlaylistRequest.build(playlist_id=playlist_id)

    assert request.endpoint == f"playlists/{playlist_id}/followers"
    assert request.method_type is HTTPMethod.DELETE
    assert AuthScope.PLAYLIST_MODIFY_PRIVATE in request.required_scopes
    assert AuthScope.PLAYLIST_MODIFY_PUBLIC in request.required_scopes

    params = request.params
    assert isinstance(params, UnfollowPlaylistRequestParams)
    assert params.playlist_id == playlist_id
    assert request.body is None
