from typing import Callable, Any
from functools import reduce

from phns.utility import get_args


# primary functions

def curry(fn: Callable) -> Callable:

    arity = len(get_args(fn))

    def retain(*old_args, **old_kwargs):

        def collect(*new_args, **new_kwargs):
            args = (*old_args, *new_args)
            kwargs = {**old_kwargs, **new_kwargs}
            return fn(*args, **kwargs) if len(args) + len(kwargs) == arity\
                else retain(*args, **kwargs)

        return collect

    return retain()

def compose(*fns: Callable) -> Callable:
    return lambda *value: reduce(
        lambda acc, fn: fn(acc),
        list(reversed(fns))[1:] if len(fns) > 1 else [],
        list(reversed(fns))[0](*value)
    )

def pipe(*fns: Callable) -> Callable:
    return lambda *value: reduce(
        lambda acc, fn: fn(acc),
        fns[1:] if len(fns) > 1 else [],
        fns[0](*value)
    )
