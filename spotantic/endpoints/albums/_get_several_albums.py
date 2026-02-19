from collections.abc import Sequence
from typing import Optional

from typing_extensions import deprecated

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.albums.requests import GetSeveralAlbumsRequest
from spotantic.models.spotify import AlbumModel
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyMarketID


@deprecated("This endpoint is deprecated since 11 February 2026 for new users (March 9 2026 for old users).")
async def get_several_albums(
    client: SpotanticClient, *, album_ids: Sequence[SpotifyItemID], market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetSeveralAlbumsRequest, APIResponse, list[AlbumModel]]:
    """Get Spotify catalog information for multiple albums identified by their Spotify IDs.

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users (March 9 2026 for old users).

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        album_ids: A list of Spotify artist IDs to retrieve.
        market: An ISO 3166-1 alpha-2 country code.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetSeveralAlbumsRequest.build(album_ids=album_ids, market=market)
    response = await client.request(request)
    assert response is not None
    data = [AlbumModel(**album_data) for album_data in response["albums"]]

    return APICallModel(request=request, response=response, data=data)
