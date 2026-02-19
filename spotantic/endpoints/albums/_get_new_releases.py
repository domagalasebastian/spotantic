from typing_extensions import deprecated

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.albums.requests import GetNewReleasesRequest
from spotantic.models.spotify import PagedResultModel
from spotantic.models.spotify import SimplifiedAlbumModel
from spotantic.types import APIResponse


@deprecated("This endpoint is deprecated since 11 February 2026 for new users (March 9 2026 for old users).")
async def get_new_releases(
    client: SpotanticClient, *, limit: int = 20, offset: int = 0
) -> APICallModel[GetNewReleasesRequest, APIResponse, PagedResultModel[SimplifiedAlbumModel]]:
    """Get a list of new album releases featured in Spotify (shown, for example, on a Spotify player’s “Browse” tab).

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users (March 9 2026 for old users).

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        limit: The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50.
        offset: The index of the first item to return. Default: 0 (the first item).
          Use with limit to get the next set of items.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetNewReleasesRequest.build(limit=limit, offset=offset)
    response = await client.request(request)
    assert response is not None
    data = PagedResultModel[SimplifiedAlbumModel](**response["albums"])

    return APICallModel(request=request, response=response, data=data)
