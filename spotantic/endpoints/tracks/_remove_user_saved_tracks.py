from collections.abc import Sequence

from typing_extensions import deprecated

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.tracks.requests import RemoveUserSavedTracksRequest
from spotantic.types import RawAPIResponse
from spotantic.types import SpotifyItemID


@deprecated("This endpoint is deprecated. Use Remove Items from Library instead.")
async def remove_user_saved_tracks(
    client: SpotanticClient, *, track_ids: Sequence[SpotifyItemID]
) -> APICallModel[RemoveUserSavedTracksRequest, RawAPIResponse, None]:
    """Remove one or more tracks from the current user's 'Your Music' library.

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users (March 9 2026 for old users).
       Use *Remove Items from Library* instead.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        track_ids: A list of the Spotify IDs for the tracks to be removed.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = RemoveUserSavedTracksRequest.build(track_ids=track_ids)
    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
