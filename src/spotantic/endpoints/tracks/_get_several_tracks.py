from collections.abc import Sequence
from typing import Optional

from typing_extensions import deprecated

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.spotify import TrackModel
from spotantic.models.tracks.requests import GetSeveralTracksRequest
from spotantic.models.tracks.responses import GetSeveralTracksResponse
from spotantic.types import JsonAPIResponse
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyMarketID


@deprecated("This endpoint is deprecated since 11 February 2026 for new users.")
async def get_several_tracks(
    client: SpotanticClient, *, track_ids: Sequence[SpotifyItemID], market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetSeveralTracksRequest, JsonAPIResponse, list[TrackModel]]:
    """Get Spotify catalog information for multiple tracks based on their Spotify IDs.

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users. Existing users may be able to
       continue using it. More information on the deprecation can be found in the Spotify API documentation:
       `Update on Developer Access and Platform Security
       <https://developer.spotify.com/blog/2026-02-06-update-on-developer-access-and-platform-security>`_.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        track_ids: A list of the Spotify IDs for the tracks.
        market: An ISO 3166-1 alpha-2 country code.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetSeveralTracksRequest.build(track_ids=track_ids, market=market)
    response = await client.request_json(request)
    data = GetSeveralTracksResponse.model_validate(response)

    return APICallModel(request=request, response=response, data=data.tracks)
