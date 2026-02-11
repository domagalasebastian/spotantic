from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.models._api_call_model import APICallModel
from pyspotify.models.albums.requests import CheckUserSavedAlbumsRequest
from pyspotify.types import APIResponse
from pyspotify.types import SpotifyItemID


async def check_user_saved_albums(
    client: PySpotifyClient, *, album_ids: Sequence[SpotifyItemID]
) -> APICallModel[CheckUserSavedAlbumsRequest, APIResponse, dict[SpotifyItemID, bool]]:
    """Check if one or more albums is already saved in the current Spotify user's 'Your Music' library.

    Args:
        client: PySpotifyClient instance.
        album_ids: A list of Spotify IDs for the albums to check.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = CheckUserSavedAlbumsRequest.build(
        album_ids=album_ids,
    )
    response = await client.request(request)
    assert response is not None
    data = dict(zip(album_ids, response))

    return APICallModel(request=request, response=response, data=data)
