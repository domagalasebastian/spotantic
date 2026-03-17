from http import HTTPMethod

from spotantic.models.users.requests import CheckIfCurrentUserFollowsPlaylistRequest
from spotantic.models.users.requests import CheckIfCurrentUserFollowsPlaylistRequestParams
from spotantic.types import SpotifyItemID


def test_check_if_current_user_follows_playlist_request(example_instances_of_type):
    playlist_id = example_instances_of_type[SpotifyItemID]
    request = CheckIfCurrentUserFollowsPlaylistRequest.build(playlist_id=playlist_id)

    assert request.endpoint == f"playlists/{playlist_id}/followers/contains"
    assert request.method_type is HTTPMethod.GET

    params = request.params
    assert isinstance(params, CheckIfCurrentUserFollowsPlaylistRequestParams)
    assert params.playlist_id == playlist_id
    assert request.body is None
