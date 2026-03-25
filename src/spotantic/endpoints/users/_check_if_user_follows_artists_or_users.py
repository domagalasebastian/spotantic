from collections.abc import Sequence

from typing_extensions import deprecated

from spotantic._utils.models._type_validation import validate_is_instance_of
from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.users.requests import CheckIfUserFollowsArtistsOrUsersRequest
from spotantic.types import JsonAPIResponse
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyItemType


@deprecated("This endpoint is deprecated. Use Check User's Saved Items instead.")
async def check_if_user_follows_artists_or_users(
    client: SpotanticClient,
    *,
    item_type: SpotifyItemType,
    item_ids: Sequence[str],
) -> APICallModel[CheckIfUserFollowsArtistsOrUsersRequest, JsonAPIResponse, dict[SpotifyItemID, bool]]:
    """Check to see if the current user is following one or more artists or other Spotify users.

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users. Existing users may be able to
       continue using it. More information on the deprecation can be found in the Spotify API documentation:
       `Update on Developer Access and Platform Security
       <https://developer.spotify.com/blog/2026-02-06-update-on-developer-access-and-platform-security>`_.
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
    response = await client.request_json(request)
    validated_response = validate_is_instance_of(response, list[bool])
    data = dict(zip(item_ids, validated_response, strict=True))

    return APICallModel(request=request, response=response, data=data)
