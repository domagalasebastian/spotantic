from collections.abc import Sequence

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.library.requests import SaveItemsToLibraryRequest
from spotantic.types import RawAPIResponse
from spotantic.types import SpotifyItemURI


async def save_items_to_library(
    client: SpotanticClient, *, uris: Sequence[SpotifyItemURI]
) -> APICallModel[SaveItemsToLibraryRequest, RawAPIResponse, None]:
    """Add one or more items to the current user's library.

    Accepts Spotify URIs for tracks, albums, episodes, shows, audiobooks, users, and playlists.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        uris: A list of the Spotify URIs for the items to be saved to the user's library.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = SaveItemsToLibraryRequest.build(
        uris=uris,
    )
    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
