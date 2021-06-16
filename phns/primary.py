from functools import reduce
from typing import Callable, Any

from phns.utility import get_args


# primary functions

def curry(fn: Callable) -> Callable:
    """
    Returns a function to which the arguments to 'fn' can be passed in part
    or full, repeatedly if part, delaying invocation until all are received.

    >>> curry(lambda x, y, z: x + y + z)(1)(2)(3)
    6
    """
    arity = len(get_args(fn))

    def retain(*old_args, **old_kwargs):

        def collect(*new_args, **new_kwargs):
            args = (*old_args, *new_args)
            kwargs = {**old_kwargs, **new_kwargs}
            return fn(*args, **kwargs) if len(args) + len(kwargs) == arity\
                else retain(*args, **kwargs)

        return collect

    return retain()

def curry_n(fn: Callable, n: int) -> Callable:
    """
    Returns a function to which 'n' arguments to 'fn' can be passed in part
    or full, repeatedly if part, delaying invocation until all are received.

    >>> sum_n = lambda *xs: reduce(lambda acc, x: acc + x, [*xs], 0)
    >>> curry_n(sum_n, 4)(1)(2)(3)(4)
    10
    """
    def retain(*old_args, **old_kwargs):

        def collect(*new_args, **new_kwargs):
            args = (*old_args, *new_args)
            kwargs = {**old_kwargs, **new_kwargs}
            return fn(*args, **kwargs) if len(args) + len(kwargs) == n\
                else retain(*args, **kwargs)

        return collect

    return retain()

def compose(*fns: Callable) -> Callable:
    """
    Returns a function invoking 'fns' in sequence right to left, the first
    with the initial arguments, each thereafter with the last return value.

    >>> compose(lambda x: x + 1, lambda x, y, z: x + y + z)(1, 2, 3)
    7
    """
    return lambda *value: reduce(
        lambda acc, fn: fn(acc),
        list(reversed(fns))[1:] if len(fns) > 1 else [],
        list(reversed(fns))[0](*value)
    )

def pipe(*fns: Callable) -> Callable:
    """
    Returns a function invoking 'fns' in sequence left to right, the first
    with the initial arguments, each thereafter with the last return value.

    >>> pipe(lambda x, y, z: x + y + z, lambda x: x + 1)(1, 2, 3)
    7
    """
    return lambda *value: reduce(
        lambda acc, fn: fn(acc),
        fns[1:] if len(fns) > 1 else [],
        fns[0](*value)
    )
