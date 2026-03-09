from http import HTTPMethod

from spotantic.models.markets.requests import GetAvailableMarketsRequest


def test_get_available_markets_request_model() -> None:
    req = GetAvailableMarketsRequest.build()

    assert req.endpoint == "markets"
    assert req.method_type is HTTPMethod.GET
    assert req.params is None
    assert req.body is None
