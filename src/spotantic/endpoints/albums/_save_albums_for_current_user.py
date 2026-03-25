from collections.abc import Sequence

from typing_extensions import deprecated

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.albums.requests import SaveAlbumsForCurrentUserRequest
from spotantic.types import RawAPIResponse
from spotantic.types import SpotifyItemID


@deprecated("This endpoint is deprecated. Use Remove Items from Library instead.")
async def save_albums_for_current_user(
    client: SpotanticClient, *, album_ids: Sequence[SpotifyItemID]
) -> APICallModel[SaveAlbumsForCurrentUserRequest, RawAPIResponse, None]:
    """Save one or more albums to the current user's 'Your Music' library.

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users. Existing users may be able to
       continue using it. More information on the deprecation can be found in the Spotify API documentation:
       `Update on Developer Access and Platform Security
       <https://developer.spotify.com/blog/2026-02-06-update-on-developer-access-and-platform-security>`_.
       Use *Save Items to Library* instead.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
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
