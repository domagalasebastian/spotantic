from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.player.requests import StartResumePlaybackRequest
from spotantic.models.player.requests import StartResumePlaybackRequestBody
from spotantic.models.player.requests._start_resume_playback import PositionOffsetModel
from spotantic.models.player.requests._start_resume_playback import URIOffsetModel
from spotantic.types import SpotifyAlbumURI
from spotantic.types import SpotifyArtistURI
from spotantic.types import SpotifyTrackURI
from tests.unit._helpers import _example_instances_of_type


def test_start_resume_playback_request_model_with_context_uri_and_offset_position() -> None:
    example_album_uri = _example_instances_of_type[SpotifyAlbumURI]

    req = StartResumePlaybackRequest.build(
        device_id="device-1",
        context_uri=example_album_uri,
        offset=1,
        position_ms=5000,
    )

    assert req.endpoint == "me/player/play"
    assert req.method_type is HTTPMethod.PUT

    body = req.body
    assert isinstance(body, StartResumePlaybackRequestBody)
    assert body.context_uri == example_album_uri
    assert body.position_ms == 5000
    assert isinstance(body.offset, PositionOffsetModel)
    assert body.offset.position == 1


def test_start_resume_playback_request_model_with_uris_and_offset_uri() -> None:
    example_track_uri = _example_instances_of_type[SpotifyTrackURI]
    other_track_uri = "spotify:track:ZzYyXxWwVvUuTtSsRrQqPp"

    req = StartResumePlaybackRequest.build(
        uris=[example_track_uri, other_track_uri],
        offset=example_track_uri,
    )

    body = req.body
    assert isinstance(body, StartResumePlaybackRequestBody)
    assert body.uris == [example_track_uri, other_track_uri]
    assert isinstance(body.offset, URIOffsetModel)
    assert body.offset.uri == example_track_uri


def test_start_resume_playback_request_model_rejects_context_and_uris_together() -> None:
    example_album_uri = _example_instances_of_type[SpotifyAlbumURI]
    example_track_uri = _example_instances_of_type[SpotifyTrackURI]

    with pytest.raises(ValidationError):
        StartResumePlaybackRequest.build(context_uri=example_album_uri, uris=[example_track_uri])


def test_start_resume_playback_request_model_rejects_offset_without_context_or_uris() -> None:
    with pytest.raises(ValidationError):
        StartResumePlaybackRequest.build(offset=1)


def test_start_resume_playback_request_model_rejects_offset_position_exceeding_uris_length() -> None:
    example_track_uri = _example_instances_of_type[SpotifyTrackURI]

    with pytest.raises(ValidationError):
        StartResumePlaybackRequest.build(uris=[example_track_uri], offset=2)


def test_start_resume_playback_request_model_rejects_offset_uri_not_in_uris() -> None:
    example_track_uri = _example_instances_of_type[SpotifyTrackURI]

    with pytest.raises(ValidationError):
        StartResumePlaybackRequest.build(uris=[example_track_uri], offset="spotify:track:ZzYyXxWwVvUuTtSsRrQqPp")


def test_start_resume_playback_request_model_rejects_offset_with_invalid_context_type() -> None:
    example_artist_uri = _example_instances_of_type[SpotifyArtistURI]

    with pytest.raises(ValidationError):
        StartResumePlaybackRequest.build(context_uri=example_artist_uri, offset=1)
