from collections.abc import Sequence

from typing_extensions import deprecated

from spotantic._utils.models._type_validation import validate_is_instance_of
from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.albums.requests import CheckUserSavedAlbumsRequest
from spotantic.types import JsonAPIResponse
from spotantic.types import SpotifyItemID


@deprecated("This endpoint is deprecated. Use Check User's Saved Items instead.")
async def check_user_saved_albums(
    client: SpotanticClient, *, album_ids: Sequence[SpotifyItemID]
) -> APICallModel[CheckUserSavedAlbumsRequest, JsonAPIResponse, dict[SpotifyItemID, bool]]:
    """Check if one or more albums is already saved in the current Spotify user's 'Your Music' library.

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users (March 9 2026 for old users).
       This endpoint is deprecated. Use *Check User's Saved Items* instead.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        album_ids: A list of Spotify IDs for the albums to check.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = CheckUserSavedAlbumsRequest.build(
        album_ids=album_ids,
    )
    response = await client.request_json(request)
    validated_response = validate_is_instance_of(response, list[bool])
    data = dict(zip(album_ids, validated_response, strict=True))

    return APICallModel(request=request, response=response, data=data)
