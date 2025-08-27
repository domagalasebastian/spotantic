from http import HTTPMethod

from pyspotify.models import RequestModel


class GetUserQueueRequest(RequestModel[None, None]):
    method_type: HTTPMethod = HTTPMethod.GET
