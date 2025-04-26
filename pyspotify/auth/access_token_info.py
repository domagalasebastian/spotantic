from __future__ import annotations
from datetime import datetime, timedelta
import json
from pathlib import Path
from typing import Literal, Any, Optional
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
            data = fd.read()

        json_data = json.loads(data)

        return cls(**json_data)
