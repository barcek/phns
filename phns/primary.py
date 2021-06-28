"""
Higher order functions both receiving one or more functions and returning one:
- for currying     curry, curry_n
- for composition  compose, pipe
"""


from functools import reduce
from typing import Callable, Any

from phns.utility import get_args


# primary functions

def curry_n(fn: Callable, n: int) -> Callable:
    """
    Returns a function to which 'n' arguments to 'fn' can be passed in part
    or full, repeatedly if part, delaying invocation until all are received.

    Used where 'fn' is of variable arity. For fixed arity, see also 'curry'.

    >>> sum_n = lambda *xs: reduce(lambda acc, x: acc + x, [*xs], 0)
    >>> curry_n(sum_n, 2)(1)(2)
    3
    """
    arity = n

    def retain(*old_args, **old_kwargs):

        def collect(*new_args, **new_kwargs):
            args = (*old_args, *new_args)
            kwargs = {**old_kwargs, **new_kwargs}
            return fn(*args, **kwargs) if len(args) + len(kwargs) == arity\
                else retain(*args, **kwargs)

        return collect

    return retain()

def curry(fn: Callable) -> Callable:
    """
    Returns a function to which the arguments to 'fn' can be passed in part
    or full, repeatedly if part, delaying invocation until all are received.

    Used where 'fn' is of fixed arity. Implements 'curry_n' for this number.

    >>> curry(lambda x, y: x + y)(1)(2)
    3
    """
    n = len(get_args(fn))
    return curry_n(fn, n)

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
