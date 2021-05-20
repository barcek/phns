from typing import TypeVar, Callable, Iterable, List, Dict, Any
from inspect import getfullargspec


# types

V = TypeVar('V')
H = Callable[[V], V]


# secondary functions

def traverse_iter(handle: H, tree: Iterable[V], const: Any = list) -> Iterable[V]:
    return const(handle(node) if not isinstance(node, const)
        else traverse_iter(handle, node, const) for node in tree)

def traverse_dict(handle: H, tree: Dict[Any, V]) -> Dict[Any, Any]:
    return dict((k, handle(v)) if not isinstance(v, dict)
        else (k, traverse_dict(handle, v)) for k, v in tree.items())

def get_args(fn: Callable) -> List[str]:
    return getfullargspec(fn).args


# tertiary functions

def get_constructor(object: Any) -> Any:
    return object.__class__

def get_class_name(object: Any) -> str:
    return str(object.__class__.__name__)
