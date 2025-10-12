from typing import Optional
from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemType
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import APICallModel
from pyspotify.models.search.requests import SearchForItemIncludeExternal
from pyspotify.models.search.requests import SearchForItemRequest
from pyspotify.models.search.responses import SearchForItemResponse


async def search_for_item(
    client: PySpotifyClient,
    *,
    query: str,
    item_type: Sequence[SpotifyItemType],
    market: Optional[SpotifyMarketID] = None,
    limit: int = 20,
    offset: int = 0,
    include_external: Optional[SearchForItemIncludeExternal] = None,
) -> APICallModel[SearchForItemRequest, APIResponse, SearchForItemResponse]:
    request = SearchForItemRequest.build(
        query=query,
        item_type=item_type,
        market=market,
        limit=limit,
        offset=offset,
        include_external=include_external,
    )
    response = await client.request(request)
    assert response is not None
    data = SearchForItemResponse(**response)

    return APICallModel(request=request, response=response, data=data)
