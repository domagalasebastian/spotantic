from __future__ import annotations

from datetime import datetime
from datetime import timedelta
from pathlib import Path
from typing import Any
from typing import Literal
from typing import Optional

from pydantic import BaseModel


class AccessTokenInfo(BaseModel):
    access_token: str
    token_type: Literal["Bearer"]
    scope: Optional[str] = None
    expires_in: int
    refresh_token: Optional[str] = None
    expires_at: Optional[datetime] = None

    def model_post_init(self, context: Any, /) -> None:
        if self.expires_at is None:
            self.expires_at = datetime.now() + timedelta(seconds=self.expires_in)

        return super().model_post_init(context)

    def store_token(self, file_path: Path) -> None:
        with open(file_path, "w") as fd:
            fd.write(self.model_dump_json())

    @classmethod
    def load_token(cls, file_path: Path) -> AccessTokenInfo:
        with open(file_path, "r") as fd:
            json_data = fd.read()

        return cls.model_validate_json(json_data=json_data)
