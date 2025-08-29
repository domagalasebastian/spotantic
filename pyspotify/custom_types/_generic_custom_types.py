from typing import Annotated

from pydantic import PlainSerializer

ParamsBool = Annotated[bool, PlainSerializer(lambda flag: str(flag).lower(), return_type=str)]
