from collections.abc import Sequence

from typing_extensions import deprecated

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.users.requests import CheckIfUserFollowsArtistsOrUsersRequest
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyItemType


@deprecated("This endpoint is deprecated. Use Check User's Saved Items instead.")
async def check_if_user_follows_artists_or_users(
    client: SpotanticClient,
    *,
    item_type: SpotifyItemType,
    item_ids: Sequence[str],
) -> APICallModel[CheckIfUserFollowsArtistsOrUsersRequest, APIResponse, dict[SpotifyItemID, bool]]:
    """Check to see if the current user is following one or more artists or other Spotify users.

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users (March 9 2026 for old users).
       This endpoint is deprecated. Use *Check User's Saved Items* instead.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        item_type: The type of item to check. Valid values are 'artist' or 'user'.
        item_ids: A list of Spotify IDs for the artists or users to check.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = CheckIfUserFollowsArtistsOrUsersRequest.build(
        item_type=item_type,
        item_ids=item_ids,
    )
    response = await client.request(request)
    assert response is not None
    data = dict(zip(item_ids, response))

    return APICallModel(request=request, response=response, data=data)
