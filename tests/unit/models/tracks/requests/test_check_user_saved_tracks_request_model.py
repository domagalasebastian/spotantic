from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.tracks.requests import CheckUserSavedTracksRequest
from spotantic.models.tracks.requests import CheckUserSavedTracksRequestParams
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID
from tests.unit._helpers import _example_instances_of_type


def test_check_user_saved_tracks_request():
    example_track_id = _example_instances_of_type[SpotifyItemID]
    track_ids = [example_track_id, example_track_id]
    request = CheckUserSavedTracksRequest.build(track_ids=track_ids)

    assert request.endpoint == "me/tracks/contains"
    assert AuthScope.USER_LIBRARY_READ in request.required_scopes
    assert request.method_type is HTTPMethod.GET

    params = request.params
    assert isinstance(params, CheckUserSavedTracksRequestParams)
    assert params.track_ids == track_ids
    assert request.body is None

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["ids"] == ",".join(track_ids)


def test_check_user_saved_tracks_request_too_many_ids():
    example_track_id = _example_instances_of_type[SpotifyItemID]
    too_many_ids = [example_track_id] * 51

    with pytest.raises(ValidationError):
        CheckUserSavedTracksRequest.build(track_ids=too_many_ids)
