from typing import TypeVar, Callable, Iterable, List, Dict, Any
from inspect import getfullargspec


# types

V = TypeVar('V')
H = Callable[[V], V]


# secondary functions

def traverse_iter(handle: H, tree: Iterable[V], const: Any = list) -> Iterable[V]:
    """
    Returns an instance of 'const' mapped from 'tree' by applying 'handle'
    to each value in an instance of 'const' not itself an instance.

    >>> traverse_iter(lambda x: x + 1, [1, [2, 3]])
    [2, [3, 4]]
    """
    return const(handle(node) if not isinstance(node, const)
        else traverse_iter(handle, node, const) for node in tree)

def traverse_dict(handle: H, tree: Dict[Any, V]) -> Dict[Any, Any]:
    """
    Returns a dictionary mapped from 'tree' by applying 'handle'
    to each value in a dictionary not itself a dictionary.

    >>> traverse_dict(lambda x: x + 1, {'a': 1, 'b': {'c': 2}})
    {'a': 2, 'b': {'c': 3}}
    """
    return dict((k, handle(v)) if not isinstance(v, dict)
        else (k, traverse_dict(handle, v)) for k, v in tree.items())

def get_args(fn: Callable) -> List[str]:
    """
    Returns a list of strings each naming a positional argument to 'fn'.

    >>> get_args(lambda x: x + 1)
    ['x']
    """
    return getfullargspec(fn).args


# tertiary functions

def get_constructor(object: Any) -> Any:
    """
    Returns the class of which 'object' is an instance.

    >>> get_constructor(1)
    <class 'int'>
    """
    return object.__class__

def get_class_name(object: Any) -> str:
    """
    Returns a string naming the class of which 'object' is an instance.

    >>> get_class_name(1)
    'int'
    """
    return str(get_constructor(object).__name__)
