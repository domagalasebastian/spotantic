from typing import Dict
from typing import Sequence

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.shows.requests import CheckUserSavedShowsRequest
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemID


async def check_user_saved_shows(
    client: SpotanticClient, *, show_ids: Sequence[SpotifyItemID]
) -> APICallModel[CheckUserSavedShowsRequest, APIResponse, Dict[SpotifyItemID, bool]]:
    """Check if given shows are saved in the user's library.

    Check if one or more shows is already saved in the current Spotify user's library.

    Args:
        client: SpotanticClient instance.
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
