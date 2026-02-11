from typing import Optional
from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.models import APICallModel
from pyspotify.models.episodes.requests import GetSeveralEpisodesRequest
from pyspotify.models.spotify import EpisodeModel
from pyspotify.types import APIResponse
from pyspotify.types import SpotifyItemID
from pyspotify.types import SpotifyMarketID


async def get_several_episodes(
    client: PySpotifyClient, *, episode_ids: Sequence[SpotifyItemID], market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetSeveralEpisodesRequest, APIResponse, list[EpisodeModel]]:
    """Get Spotify catalog information for several episodes.

    Get Spotify catalog information for several episodes based on their Spotify IDs.

    Args:
        client: PySpotifyClient instance.
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
