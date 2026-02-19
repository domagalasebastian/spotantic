from typing import Optional

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.albums.requests import GetAlbumTracksRequest
from spotantic.models.spotify import PagedResultModel
from spotantic.models.spotify import SimplifiedTrackModel
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyMarketID


async def get_album_tracks(
    client: SpotanticClient,
    *,
    album_id: SpotifyItemID,
    limit: int = 20,
    offset: int = 0,
    market: Optional[SpotifyMarketID] = None,
) -> APICallModel[GetAlbumTracksRequest, APIResponse, PagedResultModel[SimplifiedTrackModel]]:
    """Get Spotify catalog information about an album’s tracks.
    Optional parameters can be used to limit the number of tracks returned.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        album_id: The Spotify ID for the album.
        limit: The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50.
        offset: The index of the first item to return. Default: 0 (the first item).
          Use with limit to get the next set of items.
        market: An ISO 3166-1 alpha-2 country code.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetAlbumTracksRequest.build(
        album_id=album_id,
        limit=limit,
        offset=offset,
        market=market,
    )
    response = await client.request(request)
    assert response is not None
    data = PagedResultModel[SimplifiedTrackModel](**response)

    return APICallModel(request=request, response=response, data=data)
