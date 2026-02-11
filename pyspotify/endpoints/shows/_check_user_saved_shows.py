from typing import Dict
from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.models import APICallModel
from pyspotify.models.shows.requests import CheckUserSavedShowsRequest
from pyspotify.types import APIResponse
from pyspotify.types import SpotifyItemID


async def check_user_saved_shows(
    client: PySpotifyClient, *, show_ids: Sequence[SpotifyItemID]
) -> APICallModel[CheckUserSavedShowsRequest, APIResponse, Dict[SpotifyItemID, bool]]:
    """Check if given shows are saved in the user's library.

    Check if one or more shows is already saved in the current Spotify user's library.

    Args:
        client: PySpotifyClient instance.
        show_ids: A list of the Spotify IDs for the shows.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = CheckUserSavedShowsRequest.build(
        show_ids=show_ids,
    )
    response = await client.request(request)
    assert response is not None
    data = dict(zip(show_ids, response, strict=True))

    return APICallModel(request=request, response=response, data=data)
