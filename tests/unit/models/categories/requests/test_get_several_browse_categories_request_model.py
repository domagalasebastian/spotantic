from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.categories.requests import GetSeveralBrowseCategoriesRequest
from spotantic.models.categories.requests import GetSeveralBrowseCategoriesRequestParams
from spotantic.types import SpotifyLocaleID
from tests.unit._helpers import _example_instances_of_type


def test_get_several_browse_categories_request():
    locale = _example_instances_of_type[SpotifyLocaleID]
    req = GetSeveralBrowseCategoriesRequest.build(limit=10, offset=2, locale=locale)

    assert req.endpoint == "browse/categories"
    assert req.method_type is HTTPMethod.GET

    params = req.params
    assert isinstance(params, GetSeveralBrowseCategoriesRequestParams)
    assert params.limit == 10
    assert params.offset == 2
    assert params.locale == locale

    with pytest.raises(ValidationError):
        GetSeveralBrowseCategoriesRequest.build(limit=0)

    with pytest.raises(ValidationError):
        GetSeveralBrowseCategoriesRequest.build(limit=51)
