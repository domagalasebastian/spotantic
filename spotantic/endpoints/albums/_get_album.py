from typing import Optional

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.albums.requests import GetAlbumRequest
from spotantic.models.spotify import AlbumModel
from spotantic.types import JsonAPIResponse
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyMarketID


async def get_album(
    client: SpotanticClient, *, album_id: SpotifyItemID, market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetAlbumRequest, JsonAPIResponse, AlbumModel]:
    """Get Spotify catalog information for a single album.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        album_id: The Spotify ID for the album.
        market: An ISO 3166-1 alpha-2 country code.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetAlbumRequest.build(album_id=album_id, market=market)
    response = await client.request_json(request)
    data = AlbumModel.model_validate(response)

    return APICallModel(request=request, response=response, data=data)
