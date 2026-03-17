from http import HTTPMethod

from spotantic.models.episodes.requests import GetEpisodeRequest
from spotantic.models.episodes.requests import GetEpisodeRequestParams
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyMarketID


def test_get_episode_request(example_instances_of_type):
    episode_id = example_instances_of_type[SpotifyItemID]
    market = example_instances_of_type[SpotifyMarketID]
    req = GetEpisodeRequest.build(episode_id=episode_id, market=market)

    assert req.endpoint == f"episodes/{episode_id}"
    assert AuthScope.USER_READ_PLAYBACK_POSITION in req.required_scopes
    assert req.method_type is HTTPMethod.GET

    params = req.params
    assert isinstance(params, GetEpisodeRequestParams)
    assert params.episode_id == episode_id
    assert params.market == market
    assert req.body is None

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["id"] == episode_id
