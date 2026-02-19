from typing import Optional

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.episodes.requests import GetEpisodeRequest
from spotantic.models.spotify import EpisodeModel
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyMarketID


async def get_episode(
    client: SpotanticClient, *, episode_id: SpotifyItemID, market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetEpisodeRequest, APIResponse, EpisodeModel]:
    """Get Spotify catalog information for a single episode.

    Get Spotify catalog information for a single episode identified by its unique Spotify ID.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        episode_id: The Spotify ID for the episode.
        market: An ISO 3166-1 alpha-2 country code.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetEpisodeRequest.build(episode_id=episode_id, market=market)
    response = await client.request(request)
    assert response is not None
    data = EpisodeModel(**response)

    return APICallModel(request=request, response=response, data=data)
