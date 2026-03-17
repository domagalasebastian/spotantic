from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.tracks.requests import RemoveUserSavedTracksRequest
from spotantic.models.tracks.requests import RemoveUserSavedTracksRequestParams
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID


def test_remove_user_saved_tracks_request(example_instances_of_type):
    example_track_id = example_instances_of_type[SpotifyItemID]
    track_ids = [example_track_id, example_track_id]
    request = RemoveUserSavedTracksRequest.build(track_ids=track_ids)

    assert request.endpoint == "me/tracks"
    assert AuthScope.USER_LIBRARY_MODIFY in request.required_scopes
    assert request.method_type is HTTPMethod.DELETE

    params = request.params
    assert isinstance(params, RemoveUserSavedTracksRequestParams)
    assert params.track_ids == track_ids
    assert request.body is None

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["ids"] == ",".join(track_ids)


def test_remove_user_saved_tracks_request_too_many_ids(example_instances_of_type):
    example_track_id = example_instances_of_type[SpotifyItemID]
    too_many_ids = [example_track_id] * 51

    with pytest.raises(ValidationError):
        RemoveUserSavedTracksRequest.build(track_ids=too_many_ids)
