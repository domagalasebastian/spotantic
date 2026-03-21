from collections.abc import Sequence
from typing import Optional

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.search.requests import SearchForItemIncludeExternal
from spotantic.models.search.requests import SearchForItemRequest
from spotantic.models.search.responses import SearchForItemResponse
from spotantic.types import JsonAPIResponse
from spotantic.types import SpotifyItemType
from spotantic.types import SpotifyMarketID


async def search_for_item(
    client: SpotanticClient,
    *,
    query: str,
    item_type: Sequence[SpotifyItemType],
    market: Optional[SpotifyMarketID] = None,
    limit: int = 10,
    offset: int = 0,
    include_external: Optional[SearchForItemIncludeExternal] = None,
) -> APICallModel[SearchForItemRequest, JsonAPIResponse, SearchForItemResponse]:
    """Search for specified items based on a provided query.

    Get Spotify catalog information about albums, artists, playlists, tracks, shows,
    episodes or audiobooks that match a keyword string. Audiobooks are only available
    within the US, UK, Canada, Ireland, New Zealand and Australia markets.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        query: Your search query.
        item_type: A list of item types to search across. Search results include hits
          from all the specified item types.
        market: An ISO 3166-1 alpha-2 country code.
        limit: The maximum number of results to return in each item type.
        offset: The index of the first result to return. Use with limit to get
          the next page of search results.
        include_external: If set to `audio`, it signals that the client can play
          externally hosted audio content, and marks the content as playable in the response.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = SearchForItemRequest.build(
        query=query,
        item_type=item_type,
        market=market,
        limit=limit,
        offset=offset,
        include_external=include_external,
    )
    response = await client.request_json(request)
    data = SearchForItemResponse.model_validate(response)

    return APICallModel(request=request, response=response, data=data)
