from typing import TypeVar, Callable, Generic, Iterable, List, Dict, Any

from phns.utility import traverse_iter, traverse_dict, get_constructor


# types

V = TypeVar('V')
H = Callable[[V], V]


# base functor classes

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


# pointed functor classes

class PFunctor(Functor):

    @staticmethod
    def of(value: V) -> Any:
        return PFunctor(value)

    def map(self, handle: H) -> Any:
        return PFunctor.of(handle(self.value))

class PFunctorIter(FunctorIter):

    @staticmethod
    def of(value: Iterable[V], const: Any = None) -> Any:
        const = get_constructor(value) if const is None else const
        return PFunctorIter(value, const)

    def map(self, handle: H, as_tree: bool = False) -> Any:
        if as_tree:
            traversed = traverse_iter(handle, self.value, self.const)
            return PFunctorIter(traversed)
        mapped = self.const(map(handle, self.value))
        return PFunctorIter.of(mapped)

class PFunctorDict(FunctorDict):

    @staticmethod
    def of(value: Dict[Any, V]) -> Any:
        return PFunctorDict(value)

    def map(self, handle: H, as_tree: bool = False) -> Any:
        if as_tree:
            traversed = traverse_dict(handle, self.value)
            return PFunctorDict(traversed)
        mapped = {k: handle(v) for k, v in self.value.items()}
        return PFunctorDict.of(mapped)
