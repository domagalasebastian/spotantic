from typing import Any

from pydantic import TypeAdapter


def validate_is_instance_of[T](obj: Any, expected_type: type[T]) -> T:
    """Validate if the specific object is instance of given type using pydantic ``TypeAdapter``.

    Args:
        obj: Instance to be validated.
        expected_type: Expected object type.

    Returns:
        Validated object instance.
    """
    return TypeAdapter(expected_type).validate_python(obj)
