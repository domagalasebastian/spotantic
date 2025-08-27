from http import HTTPMethod

from pyspotify.models import RequestModel


class GetAvailableDevicesRequest(RequestModel[None, None]):
    method_type: HTTPMethod = HTTPMethod.GET
