from collections.abc import Sequence

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.library.requests import CheckUserSavedItemsRequest
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemURI


async def check_user_saved_items(
    client: SpotanticClient, *, uris: Sequence[SpotifyItemURI]
) -> APICallModel[CheckUserSavedItemsRequest, APIResponse, dict[SpotifyItemURI, bool]]:
    """Check if one or more items are already saved in the current user's library.

    Accepts Spotify URIs for tracks, albums, episodes, shows, audiobooks, artists, users, and playlists.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        uris: A list of Spotify URIs for the items to check.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = CheckUserSavedItemsRequest.build(uris=uris)
    response = await client.request(request)
    assert response is not None
    data = dict(zip(uris, response))

    return APICallModel(request=request, response=response, data=data)
