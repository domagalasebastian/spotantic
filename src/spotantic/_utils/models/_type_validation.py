from typing import Any
from typing import overload

from pydantic import TypeAdapter


@overload
def validate_is_instance_of[T](obj: Any, expected_type: type[T]) -> T: ...


@overload
def validate_is_instance_of(obj: Any, expected_type: object) -> Any: ...


def validate_is_instance_of(obj: Any, expected_type: object) -> Any:
    """Validate if the specific object is instance of given type using pydantic ``TypeAdapter``.

    This helper accepts both plain Python ``type`` objects (e.g. ``str``) and
    typed constructs such as ``typing.Union`` / ``typing.Optional``.

    Args:
        obj: Instance to be validated.
        expected_type: Expected object type.

    Returns:
        Validated object instance.
    """

    return TypeAdapter(expected_type).validate_python(obj)
