from http import HTTPMethod
from typing import Annotated
from typing import Optional
from typing import Sequence

from pydantic import BaseModel
from pydantic import Field

from pyspotify.models import RequestModel


class TransferPlaybackRequestBody(BaseModel):
    device_ids: Annotated[Sequence[str], Field(max_length=1)]
    play: Optional[bool] = None


class TransferPlaybackRequest(RequestModel[None, TransferPlaybackRequestBody]):
    method_type: HTTPMethod = HTTPMethod.PUT
