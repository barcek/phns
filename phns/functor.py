from typing import TypeVar, Callable, Generic, Iterable, List, Dict, Any

from phns.utility import traverse_iter, traverse_dict, get_constructor


# types

V = TypeVar('V')
H = Callable[[V], V]


# functor classes

class Functor(Generic[V]):

    def __init__(self, value: V) -> None:
        self.value = value

    def map(self, handle: H) -> Any:
        return handle(self.value)

class FunctorIter(Generic[V]):

    def __init__(self, value: Iterable[V], const: Any = None) -> None:
        self.value = value
        self.const = get_constructor(value) if const is None else const

    def map(self, handle: H, as_tree: bool = False) -> Any:
        if as_tree:
            return traverse_iter(handle, self.value, self.const)
        return self.const(map(handle, self.value))

class FunctorDict(Generic[V]):

    def __init__(self, value: Dict[Any, V]) -> None:
        self.value = value

    def map(self, handle: H, as_tree: bool = False) -> Any:
        if as_tree:
            return traverse_dict(handle, self.value)
        return {k: handle(v) for k, v in self.value.items()}
