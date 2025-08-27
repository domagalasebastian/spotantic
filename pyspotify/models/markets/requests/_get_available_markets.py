from http import HTTPMethod

from pyspotify.models import RequestModel


class GetAvailableMarketsRequest(RequestModel[None, None]):
    method_type: HTTPMethod = HTTPMethod.GET
