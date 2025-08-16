from functools import wraps
from typing import Callable
from typing import ParamSpec
from typing import TypeVar
from typing import get_type_hints

from pydantic import TypeAdapter

P = ParamSpec("P")
R = TypeVar("R")


def validate_request_params(func: Callable[P, R]) -> Callable[P, R]:
    func_type_hints = get_type_hints(func, include_extras=True)

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        for kwarg, kwarg_val in kwargs.items():
            value_type = func_type_hints.get(kwarg)
            type_adapter = TypeAdapter(value_type)

            type_adapter.validate_python(kwarg_val)

        return func(*args, **kwargs)

    return wrapper
