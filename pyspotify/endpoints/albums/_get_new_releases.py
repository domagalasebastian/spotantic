from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.models import APICallModel
from pyspotify.models.albums.requests import GetNewReleasesRequest
from pyspotify.models.albums.requests import GetNewReleasesRequestParams
from pyspotify.models.spotify import PagedResultModel
from pyspotify.models.spotify import SimplifiedAlbumModel


async def get_new_releases(
    client: PySpotifyClient, *, limit: int = 20, offset: int = 0
) -> APICallModel[GetNewReleasesRequest, APIResponse, PagedResultModel[SimplifiedAlbumModel]]:
    request = GetNewReleasesRequest(
        endpoint="browse/new-releases",
        params=GetNewReleasesRequestParams(
            limit=limit,
            offset=offset,
        ),
    )
    response = await client.request(request)
    assert response is not None
    data = PagedResultModel[SimplifiedAlbumModel](**response["albums"])

    return APICallModel(request=request, response=response, data=data)
