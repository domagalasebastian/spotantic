from http import HTTPMethod

from spotantic.models.categories.requests import GetSingleBrowseCategoryRequest
from spotantic.models.categories.requests import GetSingleBrowseCategoryRequestParams
from spotantic.types import SpotifyLocaleID


def test_get_single_browse_category_request(example_instances_of_type):
    category_id = "cat123"
    locale = example_instances_of_type[SpotifyLocaleID]
    req = GetSingleBrowseCategoryRequest.build(category_id=category_id, locale=locale)

    assert req.endpoint == f"browse/categories/{category_id}"
    assert req.method_type is HTTPMethod.GET

    params = req.params
    assert isinstance(params, GetSingleBrowseCategoryRequestParams)
    assert params.category_id == category_id
    assert params.locale == locale

    assert req.body is None
