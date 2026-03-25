from collections.abc import Sequence

from typing_extensions import deprecated

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.users.requests import UnfollowArtistsOrUsersRequest
from spotantic.types import RawAPIResponse
from spotantic.types import SpotifyItemType


@deprecated("This endpoint is deprecated. Use Remove Items from Library instead.")
async def unfollow_artists_or_users(
    client: SpotanticClient,
    *,
    item_type: SpotifyItemType,
    item_ids: Sequence[str],
) -> APICallModel[UnfollowArtistsOrUsersRequest, RawAPIResponse, None]:
    """Remove the current user as a follower of one or more artists or other Spotify users.

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users. Existing users may be able to
       continue using it. More information on the deprecation can be found in the Spotify API documentation:
       `Update on Developer Access and Platform Security
       <https://developer.spotify.com/blog/2026-02-06-update-on-developer-access-and-platform-security>`_.
       Use *Remove Items from Library* instead.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        item_type: The type of the items to unfollow. Must be either 'artist' or 'user'.
        item_ids: A sequence of Spotify IDs for the artists or users to unfollow. Maximum of 50 IDs.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = UnfollowArtistsOrUsersRequest.build(
        item_type=item_type,
        item_ids=item_ids,
    )
    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
