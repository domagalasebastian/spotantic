from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import APICallModel
from pyspotify.models.albums.requests import RemoveUserSavedAlbumsRequest


async def remove_user_saved_albums(
    client: PySpotifyClient, *, album_ids: Sequence[SpotifyItemID]
) -> APICallModel[RemoveUserSavedAlbumsRequest, APIResponse, None]:
    """Remove one or more albums from the current user's 'Your Music' library.

    Args:
        client: PySpotifyClient instance.
        album_ids: A list of Spotify IDs for the albums to be removed from the user's library.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = RemoveUserSavedAlbumsRequest.build(
        album_ids=album_ids,
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
