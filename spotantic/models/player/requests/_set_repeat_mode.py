from __future__ import annotations

from http import HTTPMethod
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict

from spotantic.models import RequestModel
from spotantic.types import AuthScope
from spotantic.types import RepeatMode


class SetRepeatModeRequestParams(BaseModel):
    """Params model for Set Repeat Mode request."""

    model_config = ConfigDict(use_enum_values=True)

    state: RepeatMode
    """The repeat mode to set."""

    device_id: Optional[str] = None
    """The id of the device this command is targeting."""


class SetRepeatModeRequest(RequestModel[SetRepeatModeRequestParams, None]):
    """Request model for Set Repeat Mode endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.USER_MODIFY_PLAYBACK_STATE}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.PUT
    """HTTP method for the request."""

    endpoint: Optional[str] = "me/player/repeat"
    """Endpoint associated with the request."""

    @classmethod
    def build(
        cls,
        *,
        state: RepeatMode,
        device_id: Optional[str] = None,
    ) -> SetRepeatModeRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            state: The repeat mode to set.
            device_id: The id of the device this command is targeting.

        Returns:
            Validated Request object.
        """
        params = SetRepeatModeRequestParams(
            state=state,
            device_id=device_id,
        )

        return cls(params=params)
