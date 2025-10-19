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
    """Search for specified items based on a provided query.

    Get Spotify catalog information about albums, artists, playlists, tracks, shows,
    episodes or audiobooks that match a keyword string. Audiobooks are only available
    within the US, UK, Canada, Ireland, New Zealand and Australia markets.

    Args:
        client: PySpotifyClient instance.
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
    response = await client.request(request)
    assert response is not None
    data = SearchForItemResponse(**response)

    return APICallModel(request=request, response=response, data=data)
