from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.models import APICallModel
from pyspotify.models.shows.requests import GetShowEpisodesRequest
from pyspotify.models.spotify import PagedResultModel
from pyspotify.models.spotify import SimplifiedEpisodeModel
from pyspotify.types import APIResponse
from pyspotify.types import SpotifyItemID
from pyspotify.types import SpotifyMarketID


async def get_show_episodes(
    client: PySpotifyClient,
    *,
    show_id: SpotifyItemID,
    limit: int = 20,
    offset: int = 0,
    market: Optional[SpotifyMarketID] = None,
) -> APICallModel[GetShowEpisodesRequest, APIResponse, PagedResultModel[SimplifiedEpisodeModel]]:
    """Return episodes for a show.

    Get Spotify catalog information about an show’s episodes.
    Optional parameters can be used to limit the number of episodes returned.

    Args:
        client: PySpotifyClient instance.
        show_id: The Spotify ID for the show.
        limit: The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50.
        offset: The index of the first item to return. Default: 0 (the first item).
          Use with limit to get the next set of items.
        market: An ISO 3166-1 alpha-2 country code.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetShowEpisodesRequest.build(
        show_id=show_id,
        limit=limit,
        offset=offset,
        market=market,
    )
    response = await client.request(request)
    assert response is not None
    data = PagedResultModel[SimplifiedEpisodeModel](**response)

    return APICallModel(request=request, response=response, data=data)
