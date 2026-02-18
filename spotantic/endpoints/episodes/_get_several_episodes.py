from typing import Optional
from typing import Sequence

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.episodes.requests import GetSeveralEpisodesRequest
from spotantic.models.spotify import EpisodeModel
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyMarketID


async def get_several_episodes(
    client: SpotanticClient, *, episode_ids: Sequence[SpotifyItemID], market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetSeveralEpisodesRequest, APIResponse, list[EpisodeModel]]:
    """Get Spotify catalog information for several episodes.

    Get Spotify catalog information for several episodes based on their Spotify IDs.

    Args:
        client: SpotanticClient instance.
        episode_ids: A list of Spotify IDs for the episodes.
        market: An ISO 3166-1 alpha-2 country code.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetSeveralEpisodesRequest.build(episode_ids=episode_ids, market=market)
    response = await client.request(request)
    assert response is not None
    data = [EpisodeModel(**episode_data) for episode_data in response["episodes"]]

    return APICallModel(request=request, response=response, data=data)
