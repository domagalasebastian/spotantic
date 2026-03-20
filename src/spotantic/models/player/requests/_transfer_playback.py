from __future__ import annotations

from collections.abc import Sequence
from http import HTTPMethod
from typing import Annotated
from typing import Optional

from pydantic import Field

from spotantic.models import RequestBodyJsonModel
from spotantic.models import RequestHeadersModel
from spotantic.models import RequestModel
from spotantic.types import AuthScope


class TransferPlaybackRequestBody(RequestBodyJsonModel):
    """Body model for Transfer Playback request."""

    device_ids: Annotated[Sequence[str], Field(max_length=1)]
    """A list of device IDs to transfer playback to."""

    play: Optional[bool] = None
    """True to start playback on the new device. If false or not provided,
    the user's current playback will continue on the previous device."""


class TransferPlaybackRequest(RequestModel[None, TransferPlaybackRequestBody]):
    """Request model for Transfer Playback endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.USER_MODIFY_PLAYBACK_STATE}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.PUT
    """HTTP method for the request."""

    endpoint: Optional[str] = "me/player"
    """Endpoint associated with the request."""

    headers: RequestHeadersModel = RequestHeadersModel(content_type="application/json")
    """Headers for the request."""

    @classmethod
    def build(
        cls,
        *,
        device_ids: Sequence[str],
        play: Optional[bool] = None,
    ) -> TransferPlaybackRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            device_ids: A list of device IDs to transfer playback to.
            play: True to start playback on the new device. If false or not provided,
             the user's current playback will continue on the previous device.

        Returns:
            Validated Request object.
        """
        body = TransferPlaybackRequestBody(
            device_ids=device_ids,
            play=play,
        )

        return cls(body=body)
