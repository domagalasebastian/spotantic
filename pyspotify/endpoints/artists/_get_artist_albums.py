from typing import Optional
from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.models import APICallModel
from pyspotify.models.artists.requests import GetArtistAlbumsRequest
from pyspotify.models.spotify import PagedResultModel
from pyspotify.models.spotify import SimplifiedAlbumModel
from pyspotify.types import AlbumTypes
from pyspotify.types import APIResponse
from pyspotify.types import SpotifyItemID
from pyspotify.types import SpotifyMarketID


async def get_artist_albums(
    client: PySpotifyClient,
    *,
    artist_id: SpotifyItemID,
    limit: int = 20,
    offset: int = 0,
    market: Optional[SpotifyMarketID] = None,
    include_groups: Optional[Sequence[AlbumTypes]] = None,
) -> APICallModel[GetArtistAlbumsRequest, APIResponse, PagedResultModel[SimplifiedAlbumModel]]:
    """Get Spotify catalog information about an artist's albums.

    Args:
        client: PySpotifyClient instance.
        artist_id: The Spotify ID for the artist.
        limit: The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50.
        offset: The index of the first item to return. Default: 0 (the first item).
          Use with limit to get the next set of items.
        market: An ISO 3166-1 alpha-2 country code.
        include_groups: A list of keywords that will be used to filter the response.
         If not supplied, all album types will be returned.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetArtistAlbumsRequest.build(
        artist_id=artist_id,
        limit=limit,
        offset=offset,
        market=market,
        include_groups=include_groups,
    )
    response = await client.request(request)
    assert response is not None
    data = PagedResultModel[SimplifiedAlbumModel](**response)

    return APICallModel(request=request, response=response, data=data)
