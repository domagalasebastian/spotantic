from http import HTTPMethod

from spotantic.models.player.requests import GetUserQueueRequest
from spotantic.types import AuthScope


def test_get_user_queue_request_model() -> None:
    req = GetUserQueueRequest.build()

    assert req.endpoint == "me/player/queue"
    assert AuthScope.USER_READ_CURRENTLY_PLAYING in req.required_scopes
    assert AuthScope.USER_READ_PLAYBACK_STATE in req.required_scopes
    assert req.method_type is HTTPMethod.GET
    assert req.params is None
    assert req.body is None
