from typing import Literal
from typing import Union
from typing import overload

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.spotify import ArtistModel
from spotantic.models.spotify import PagedResultModel
from spotantic.models.spotify import TrackModel
from spotantic.models.users.requests import GetUserTopItemsRequest
from spotantic.models.users.requests import GetUserTopItemsTimeRange
from spotantic.models.users.requests import GetUserTopItemsType
from spotantic.types import JsonAPIResponse


@overload
async def get_user_top_items(
    client: SpotanticClient,
    *,
    item_type: Literal[GetUserTopItemsType.ARTISTS],
    time_range: GetUserTopItemsTimeRange,
    limit: int = 20,
    offset: int = 0,
) -> APICallModel[GetUserTopItemsRequest, JsonAPIResponse, PagedResultModel[ArtistModel]]: ...


@overload
async def get_user_top_items(
    client: SpotanticClient,
    *,
    item_type: Literal[GetUserTopItemsType.TRACKS],
    time_range: GetUserTopItemsTimeRange,
    limit: int = 20,
    offset: int = 0,
) -> APICallModel[GetUserTopItemsRequest, JsonAPIResponse, PagedResultModel[TrackModel]]: ...


async def get_user_top_items(
    client: SpotanticClient,
    *,
    item_type: GetUserTopItemsType,
    time_range: GetUserTopItemsTimeRange,
    limit: int = 20,
    offset: int = 0,
) -> APICallModel[
    GetUserTopItemsRequest, JsonAPIResponse, Union[PagedResultModel[ArtistModel], PagedResultModel[TrackModel]]
]:
    """Get the current user's top artists or tracks based on calculated affinity.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        item_type: The type of item to retrieve (artists or tracks).
        time_range: Over what time frame the affinities are computed.
        limit: The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50.
        offset: The index of the first item to return. Default: 0 (the first item).
          Use with limit to get the next set of items.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetUserTopItemsRequest.build(
        item_type=item_type,
        time_range=time_range,
        limit=limit,
        offset=offset,
    )
    response = await client.request_json(request)
    match item_type:
        case GetUserTopItemsType.ARTISTS:
            data = PagedResultModel[ArtistModel].model_validate(response)
        case GetUserTopItemsType.TRACKS:
            data = PagedResultModel[TrackModel].model_validate(response)

    return APICallModel(request=request, response=response, data=data)
