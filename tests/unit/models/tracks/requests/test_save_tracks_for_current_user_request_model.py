from datetime import datetime
from datetime import timezone
from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.tracks.requests import SaveTracksForCurrentUserRequest
from spotantic.models.tracks.requests import SaveTracksForCurrentUserRequestBody
from spotantic.models.tracks.requests._save_tracks_for_current_user import TimestampTrackIDModel
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID


def test_save_tracks_for_current_user_request_with_track_ids(example_instances_of_type):
    example_track_id = example_instances_of_type[SpotifyItemID]
    track_ids = [example_track_id, example_track_id]
    request = SaveTracksForCurrentUserRequest.build(track_ids=track_ids)

    assert request.endpoint == "me/tracks"
    assert AuthScope.USER_LIBRARY_MODIFY in request.required_scopes
    assert request.method_type is HTTPMethod.PUT

    body = request.body
    assert isinstance(body, SaveTracksForCurrentUserRequestBody)
    assert body.track_ids == track_ids
    assert body.timestamped_ids is None
    assert request.params is None

    body_dump = body.model_dump(by_alias=True)
    assert body_dump["ids"] == track_ids


def test_save_tracks_for_current_user_request_with_timestamped_ids(example_instances_of_type):
    example_track_id = example_instances_of_type[SpotifyItemID]
    now = datetime.now(timezone.utc)
    timestamped_ids = {example_track_id: now}
    request = SaveTracksForCurrentUserRequest.build(timestamped_ids=timestamped_ids)

    assert request.endpoint == "me/tracks"
    assert AuthScope.USER_LIBRARY_MODIFY in request.required_scopes
    assert request.method_type is HTTPMethod.PUT

    body = request.body
    assert isinstance(body, SaveTracksForCurrentUserRequestBody)
    assert body.track_ids is None
    assert body.timestamped_ids is not None
    assert all(isinstance(item, TimestampTrackIDModel) for item in body.timestamped_ids)
    assert request.params is None


def test_save_tracks_for_current_user_request_too_many_ids(example_instances_of_type):
    example_track_id = example_instances_of_type[SpotifyItemID]
    too_many_ids = [example_track_id] * 51

    with pytest.raises(ValidationError):
        SaveTracksForCurrentUserRequest.build(track_ids=too_many_ids)


def test_save_tracks_for_current_user_request_no_ids():
    with pytest.raises(ValidationError):
        SaveTracksForCurrentUserRequest.build()
