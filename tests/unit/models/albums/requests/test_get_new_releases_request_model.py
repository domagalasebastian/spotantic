from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.albums.requests import GetNewReleasesRequest
from spotantic.models.albums.requests import GetNewReleasesRequestParams


def test_get_new_releases_request():
    limit = 20
    offset = 0
    req = GetNewReleasesRequest.build(limit=limit, offset=offset)

    assert req.endpoint == "browse/new-releases"
    assert req.method_type is HTTPMethod.GET

    params = req.params
    assert isinstance(params, GetNewReleasesRequestParams)
    assert params.limit == limit
    assert params.offset == offset

    with pytest.raises(ValidationError):
        GetNewReleasesRequest.build(
            limit=0,
        )

    with pytest.raises(ValidationError):
        GetNewReleasesRequest.build(
            limit=51,
        )
