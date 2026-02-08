from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.models import APICallModel
from pyspotify.models.albums.requests import GetNewReleasesRequest
from pyspotify.models.spotify import PagedResultModel
from pyspotify.models.spotify import SimplifiedAlbumModel


async def get_new_releases(
    client: PySpotifyClient, *, limit: int = 20, offset: int = 0
) -> APICallModel[GetNewReleasesRequest, APIResponse, PagedResultModel[SimplifiedAlbumModel]]:
    """Get a list of new album releases featured in Spotify (shown, for example, on a Spotify player’s “Browse” tab).

    Args:
        client: PySpotifyClient instance.
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
