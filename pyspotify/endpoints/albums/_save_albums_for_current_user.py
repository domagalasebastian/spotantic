from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import APICallModel
from pyspotify.models.albums.requests import SaveAlbumsForCurrentUserRequest


async def save_albums_for_current_user(
    client: PySpotifyClient, *, album_ids: Sequence[SpotifyItemID]
) -> APICallModel[SaveAlbumsForCurrentUserRequest, APIResponse, None]:
    """Save one or more albums to the current user's 'Your Music' library.

    Args:
        client: PySpotifyClient instance.
        album_ids: A list of the Spotify IDs for the albums to be saved to the user's library.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = SaveAlbumsForCurrentUserRequest.build(
        album_ids=album_ids,
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
