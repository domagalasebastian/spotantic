from http import HTTPMethod

from spotantic.models.shows.requests import GetShowRequest
from spotantic.models.shows.requests import GetShowRequestParams
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID
from tests.unit._helpers import _example_instances_of_type


def test_get_show_request_model_serializes_params():
    example_id = _example_instances_of_type[SpotifyItemID]
    req = GetShowRequest.build(show_id=example_id, market="US")

    assert req.endpoint == f"shows/{example_id}"
    assert AuthScope.USER_READ_PLAYBACK_POSITION in req.required_scopes
    assert req.method_type is HTTPMethod.GET

    params = req.params
    assert isinstance(params, GetShowRequestParams)
    assert params.show_id == example_id
    assert params.market == "US"
