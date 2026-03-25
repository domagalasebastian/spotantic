from collections.abc import Sequence

from typing_extensions import deprecated

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.artists.requests import GetSeveralArtistsRequest
from spotantic.models.artists.responses import GetSeveralArtistsResponse
from spotantic.models.spotify import ArtistModel
from spotantic.types import JsonAPIResponse
from spotantic.types import SpotifyItemID


@deprecated("This endpoint is deprecated since 11 February 2026 for new users.")
async def get_several_artists(
    client: SpotanticClient, *, artist_ids: Sequence[SpotifyItemID]
) -> APICallModel[GetSeveralArtistsRequest, JsonAPIResponse, list[ArtistModel]]:
    """Get Spotify catalog information for several artists based on their Spotify IDs.

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users. Existing users may be able to
       continue using it. More information on the deprecation can be found in the Spotify API documentation:
       `Update on Developer Access and Platform Security
       <https://developer.spotify.com/blog/2026-02-06-update-on-developer-access-and-platform-security>`_.

    Args:
        client: :class:`SpotanticClient` instance.
        artist_ids: A list of Spotify artist IDs to retrieve.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetSeveralArtistsRequest.build(
        artist_ids=artist_ids,
    )
    response = await client.request_json(request)
    data = GetSeveralArtistsResponse.model_validate(response)

    return APICallModel(request=request, response=response, data=data.artists)
