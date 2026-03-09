from collections.abc import Sequence
from typing import Optional

from typing_extensions import deprecated

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.episodes.requests import GetSeveralEpisodesRequest
from spotantic.models.episodes.responses import GetSeveralEpisodesResponse
from spotantic.models.spotify import EpisodeModel
from spotantic.types import JsonAPIResponse
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyMarketID


@deprecated("This endpoint is deprecated since 11 February 2026 for new users (March 9 2026 for old users).")
async def get_several_episodes(
    client: SpotanticClient, *, episode_ids: Sequence[SpotifyItemID], market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetSeveralEpisodesRequest, JsonAPIResponse, list[EpisodeModel]]:
    """Get Spotify catalog information for several episodes based on their Spotify IDs.

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users (March 9 2026 for old users).

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        episode_ids: A list of Spotify IDs for the episodes.
        market: An ISO 3166-1 alpha-2 country code.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetSeveralEpisodesRequest.build(episode_ids=episode_ids, market=market)
    response = await client.request_json(request)
    data = GetSeveralEpisodesResponse.model_validate(response)

    return APICallModel(request=request, response=response, data=data.episodes)
