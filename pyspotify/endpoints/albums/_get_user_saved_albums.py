from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import APICallModel
from pyspotify.models.albums.requests import GetUserSavedAlbumsRequest
from pyspotify.models.spotify import PagedResultModel
from pyspotify.models.spotify import SavedAlbumModel


async def get_user_saved_albums(
    client: PySpotifyClient, *, limit: int = 20, offset: int = 0, market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetUserSavedAlbumsRequest, APIResponse, PagedResultModel[SavedAlbumModel]]:
    """Get a list of the albums saved in the current Spotify user's 'Your Music' library.

    Args:
        client: PySpotifyClient instance.
        limit: The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50.
        offset: The index of the first item to return. Default: 0 (the first item).
          Use with limit to get the next set of items.
        market: An ISO 3166-1 alpha-2 country code.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetUserSavedAlbumsRequest.build(
        limit=limit,
        offset=offset,
        market=market,
    )
    response = await client.request(request)
    assert response is not None
    data = PagedResultModel[SavedAlbumModel](**response)

    return APICallModel(request=request, response=response, data=data)
