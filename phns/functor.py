from typing import TypeVar, Callable, Generic, Iterable, List, Dict, Any

from phns.utility import traverse_iter, traverse_dict, get_constructor


# types

V = TypeVar('V')
H = Callable[[V], V]


# base functor classes

class Functor(Generic[V]):

    def __init__(self, value: V) -> None:
        """Returns a Functor instance with a value property set to 'value'.
           >>> f = Functor(1)
           >>> print(f.__class__.__name__, f.value)
           Functor 1
        """
        self.value = value

    def map(self, handle: H) -> Any:
        """Returns the instance value property having had 'handle' applied.
           >>> f = Functor(1)
           >>> print(f.map(lambda x: x + 1))
           2
        """
        return handle(self.value)

class FunctorIter(Generic[V]):

    def __init__(self, value: Iterable[V], const: Any = None) -> None:
        """Returns a FunctorIter instance with a value property set to 'value'
           and a const property set to 'const' or the constructor of 'value'.
           >>> f = FunctorIter([1, [2, 3]])
           >>> print(f.__class__.__name__, f.value, f.const == list)
           FunctorIter [1, [2, 3]] True
        """
        self.value = value
        self.const = get_constructor(value) if const is None else const

    def map(self, handle: H, as_tree: bool = False) -> Any:
        """Returns the instance value property having had 'handle' applied
           to the whole by default or to each node if 'as_tree' is True.
           >>> f = FunctorIter([1, [2, 3]])
           >>> print(f.map(lambda x: x + 1, True))
           [2, [3, 4]]
        """
        if as_tree:
            return traverse_iter(handle, self.value, self.const)
        return self.const(map(handle, self.value))

class FunctorDict(Generic[V]):

    def __init__(self, value: Dict[Any, V]) -> None:
        """Returns a FunctorDict instance with a value property set to 'value'.
           >>> f = FunctorDict({'a': 1, 'b': {'c': 2, 'd': 3}})
           >>> print(f.__class__.__name__, f.value)
           FunctorDict {'a': 1, 'b': {'c': 2, 'd': 3}}
        """
        self.value = value

    def map(self, handle: H, as_tree: bool = False) -> Any:
        """Returns the instance value property having had 'handle' applied
           to the whole by default or to each node if 'as_tree' is True.
           >>> f = FunctorDict({'a': 1, 'b': {'c': 2, 'd': 3}})
           >>> print(f.map(lambda x: x + 1, True))
           {'a': 2, 'b': {'c': 3, 'd': 4}}
        """
        if as_tree:
            return traverse_dict(handle, self.value)
        return {k: handle(v) for k, v in self.value.items()}


# pointed functor classes

class PFunctor(Functor):

    @staticmethod
    def of(value: V) -> Any:
        """Returns a PFunctor instance with a value property set to 'value'.
           >>> pf = PFunctor.of(1)
           >>> print(pf.__class__.__name__, pf.value)
           PFunctor 1
        """
        return PFunctor(value)

    def map(self, handle: H) -> Any:
        """Returns a new PFunctor instance with a value property being the
           previous instance value property having had 'handle' applied.
           >>> pf = PFunctor(1)
           >>> print(pf.map(lambda x: x + 1).value)
           2
        """
        return PFunctor.of(handle(self.value))

class PFunctorIter(FunctorIter):

    @staticmethod
    def of(value: Iterable[V], const: Any = None) -> Any:
        """Returns a PFunctorIter instance with a value property set to 'value'
           and a const property set to 'const' or the constructor of 'value'.
           >>> pf = PFunctorIter([1, [2, 3]])
           >>> print(pf.__class__.__name__, pf.value, pf.const == list)
           PFunctorIter [1, [2, 3]] True
        """
        const = get_constructor(value) if const is None else const
        return PFunctorIter(value, const)

    def map(self, handle: H, as_tree: bool = False) -> Any:
        """Returns a new PFunctorIter instance with a value property being the
           previous instance value property having had 'handle' applied
           to the whole by default or to each node if 'as_tree' is True.
           >>> pf = PFunctorIter([1, [2, 3]])
           >>> print(pf.map(lambda x: x + 1, True).value)
           [2, [3, 4]]
        """
        if as_tree:
            traversed = traverse_iter(handle, self.value, self.const)
            return PFunctorIter(traversed)
        mapped = self.const(map(handle, self.value))
        return PFunctorIter.of(mapped)

class PFunctorDict(FunctorDict):

    @staticmethod
    def of(value: Dict[Any, V]) -> Any:
        """Returns a PFunctorDict instance with a value property set to 'value'.
           >>> pf = PFunctorDict({'a': 1, 'b': {'c': 2, 'd': 3}})
           >>> print(pf.__class__.__name__, pf.value)
           PFunctorDict {'a': 1, 'b': {'c': 2, 'd': 3}}
        """
        return PFunctorDict(value)

    def map(self, handle: H, as_tree: bool = False) -> Any:
        """Returns a new PFunctorDict instance with a value property being the
           previous instance value property having had 'handle' applied
           to the whole by default or to each node if 'as_tree' is True.
           >>> pf = PFunctorDict({'a': 1, 'b': {'c': 2, 'd': 3}})
           >>> print(pf.map(lambda x: x + 1, True).value)
           {'a': 2, 'b': {'c': 3, 'd': 4}}
        """
        if as_tree:
            traversed = traverse_dict(handle, self.value)
            return PFunctorDict(traversed)
        mapped = {k: handle(v) for k, v in self.value.items()}
        return PFunctorDict.of(mapped)
