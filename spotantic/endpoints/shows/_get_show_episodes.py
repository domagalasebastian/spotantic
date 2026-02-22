from typing import Optional

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.shows.requests import GetShowEpisodesRequest
from spotantic.models.spotify import PagedResultModel
from spotantic.models.spotify import SimplifiedEpisodeModel
from spotantic.types import JsonAPIResponse
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyMarketID


async def get_show_episodes(
    client: SpotanticClient,
    *,
    show_id: SpotifyItemID,
    limit: int = 20,
    offset: int = 0,
    market: Optional[SpotifyMarketID] = None,
) -> APICallModel[GetShowEpisodesRequest, JsonAPIResponse, PagedResultModel[SimplifiedEpisodeModel]]:
    """Return episodes for a show.

    Get Spotify catalog information about an show’s episodes.
    Optional parameters can be used to limit the number of episodes returned.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
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
    response = await client.request_json(request)
    data = PagedResultModel[SimplifiedEpisodeModel].model_validate(response)

    return APICallModel(request=request, response=response, data=data)
