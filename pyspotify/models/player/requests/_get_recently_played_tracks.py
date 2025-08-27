from __future__ import annotations

from http import HTTPMethod
from typing import Annotated
from typing import Optional

from pydantic import BaseModel
from pydantic import Field
from pydantic import model_validator

from pyspotify.models import RequestModel


class GetRecentlyPlayedTracksRequestParams(BaseModel):
    limit: Annotated[int, Field(ge=1, le=50)]
    after: Optional[int] = None
    before: Optional[int] = None

    @model_validator(mode="after")
    def check_only_cursor_is_given(self) -> GetRecentlyPlayedTracksRequestParams:
        if self.after is not None and self.before is not None:
            raise ValueError("Specify either a before or after parameter, but not both!")

        return self


class GetRecentlyPlayedTracksRequest(RequestModel[GetRecentlyPlayedTracksRequestParams, None]):
    method_type: HTTPMethod = HTTPMethod.GET
