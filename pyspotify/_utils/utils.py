from typing import Any
from typing import Dict
from typing import Mapping


def drop_items_with_none_values(mapping: Mapping[Any, Any]) -> Dict[Any, Any]:
    return {key: value for key, value in mapping.items() if value is not None}
