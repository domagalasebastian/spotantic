from collections.abc import Sequence

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.library.requests import RemoveItemsFromLibraryRequest
from spotantic.types import RawAPIResponse
from spotantic.types import SpotifyItemURI


async def remove_items_from_library(
    client: SpotanticClient, *, uris: Sequence[SpotifyItemURI]
) -> APICallModel[RemoveItemsFromLibraryRequest, RawAPIResponse, None]:
    """Remove one or more items from the current user's library.

    Accepts Spotify URIs for tracks, albums, episodes, shows, audiobooks, users, and playlists.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        uris: A list of Spotify URIs for the items to be removed from the user's library.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = RemoveItemsFromLibraryRequest.build(
        uris=uris,
    )
    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
