from collections.abc import Sequence

from typing_extensions import deprecated

from spotantic._utils.models._type_validation import validate_is_instance_of
from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.episodes.requests import CheckUserSavedEpisodesRequest
from spotantic.types import JsonAPIResponse
from spotantic.types import SpotifyItemID


@deprecated("This endpoint is deprecated. Use Check User's Saved Items instead.")
async def check_user_saved_episodes(
    client: SpotanticClient, *, episode_ids: Sequence[SpotifyItemID]
) -> APICallModel[CheckUserSavedEpisodesRequest, JsonAPIResponse, dict[SpotifyItemID, bool]]:
    """Check if one or more episodes is already saved in the current Spotify user's 'Your Episodes' library.

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users. Existing users may be able to
       continue using it. More information on the deprecation can be found in the Spotify API documentation:
       `Update on Developer Access and Platform Security
       <https://developer.spotify.com/blog/2026-02-06-update-on-developer-access-and-platform-security>`_.
       This endpoint is deprecated. Use *Check User's Saved Items* instead.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        episode_ids: A list of Spotify IDs for the episodes to check.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = CheckUserSavedEpisodesRequest.build(episode_ids=episode_ids)
    response = await client.request_json(request)
    validated_response = validate_is_instance_of(response, list[bool])
    data = dict(zip(episode_ids, validated_response, strict=True))

    return APICallModel(request=request, response=response, data=data)
