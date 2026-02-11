from __future__ import annotations

from http import HTTPMethod
from typing import Optional
from typing import Union

from pydantic import BaseModel

from pyspotify.models import RequestModel
from pyspotify.types import AuthScope
from pyspotify.types import SpotifyEpisodeURI
from pyspotify.types import SpotifyTrackURI


class AddItemToPlaybackQueueRequestParams(BaseModel):
    """Params model for Add Item To Playback Queue request."""

    uri: Union[SpotifyEpisodeURI, SpotifyTrackURI]
    """The Spotify URI of the item to add to the queue"""

    device_id: Optional[str] = None
    """The id of the device this command is targeting."""


class AddItemToPlaybackQueueRequest(RequestModel[AddItemToPlaybackQueueRequestParams, None]):
    """Request model for Add Item To Playback Queue request."""

    required_scopes: set[AuthScope] = {AuthScope.USER_MODIFY_PLAYBACK_STATE}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.POST
    """HTTP method type for the request."""

    endpoint: Optional[str] = "me/player/queue"
    """Endpoint associated with the request."""

    @classmethod
    def build(
        cls,
        *,
        uri: Union[SpotifyEpisodeURI, SpotifyTrackURI],
        device_id: Optional[str] = None,
    ) -> AddItemToPlaybackQueueRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            uri: The Spotify URI of the item to add to the queue.
            device_id: The id of the device this command is targeting.

        Returns:
            Validated Request object.
        """
        params = AddItemToPlaybackQueueRequestParams(
            uri=uri,
            device_id=device_id,
        )

        return cls(params=params)
