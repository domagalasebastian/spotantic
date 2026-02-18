from typing import Sequence

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.albums.requests import SaveAlbumsForCurrentUserRequest
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemID


async def save_albums_for_current_user(
    client: SpotanticClient, *, album_ids: Sequence[SpotifyItemID]
) -> APICallModel[SaveAlbumsForCurrentUserRequest, APIResponse, None]:
    """Save one or more albums to the current user's 'Your Music' library.

    Args:
        client: SpotanticClient instance.
        album_ids: A list of the Spotify IDs for the albums to be saved to the user's library.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = SaveAlbumsForCurrentUserRequest.build(
        album_ids=album_ids,
    )
    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
