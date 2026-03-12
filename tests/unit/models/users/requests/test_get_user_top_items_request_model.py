from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.users.requests import GetUserTopItemsRequest
from spotantic.models.users.requests import GetUserTopItemsRequestParams
from spotantic.models.users.requests import GetUserTopItemsTimeRange
from spotantic.models.users.requests import GetUserTopItemsType
from spotantic.types import AuthScope


@pytest.mark.parametrize("item_type", [GetUserTopItemsType.ARTISTS, GetUserTopItemsType.TRACKS])
@pytest.mark.parametrize("time_range", list(GetUserTopItemsTimeRange))
def test_get_user_top_items_request_valid_combinations(item_type, time_range):
    request = GetUserTopItemsRequest.build(item_type=item_type, time_range=time_range)

    assert request.endpoint == f"me/top/{item_type}"
    assert request.method_type is HTTPMethod.GET
    assert AuthScope.PLAYLIST_READ_PRIVATE in request.required_scopes

    params = request.params
    assert isinstance(params, GetUserTopItemsRequestParams)
    assert params.item_type == item_type
    assert params.time_range == time_range
    assert params.limit == 20
    assert params.offset == 0
    assert request.body is None

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["type"] == item_type.value
    assert params_dump["time_range"] == time_range.value


def test_get_user_top_items_request_limit_too_high():
    with pytest.raises(ValidationError):
        GetUserTopItemsRequest.build(
            item_type=GetUserTopItemsType.ARTISTS,
            limit=51,
        )


def test_get_user_top_items_request_limit_too_low():
    with pytest.raises(ValidationError):
        GetUserTopItemsRequest.build(
            item_type=GetUserTopItemsType.ARTISTS,
            limit=0,
        )


def test_get_user_top_items_request_offset_negative():
    with pytest.raises(ValidationError):
        GetUserTopItemsRequest.build(
            item_type=GetUserTopItemsType.ARTISTS,
            offset=-1,
        )
