"""
Functor classes, available also via 'phns/builder.py' and 'phns/factory.py':
- base functor classes (Functor, FunctorIter, FunctorDict)
- pointed functor classes (PFunctor, PFunctorIter, PFunctorDict).
"""


from typing import TypeVar, Callable, Generic, Iterable, List, Dict, Any

from phns.utility import traverse_iter, traverse_dict, get_const


# types

V = TypeVar('V')
H = Callable[[V], V]


# base functor classes

class Functor(Generic[V]):
    """
    Stores a value of any type to be mapped by use of a handler function.

    value (attribute) V
      A value of any type provided for transformation via the map method.

    map (method) handle: H -> Any
      Returns the instance value property once 'handle' has been applied.
    """

    def __init__(self, value: V) -> None:
        """
        Returns a Functor instance with a value property set to 'value'.

        >>> f = Functor(1)
        >>> print(f.__class__.__name__, f.value)
        Functor 1
        """
        self.value = value

    def map(self, handle: H) -> Any:
        """
        Returns the instance value property once 'handle' has been applied.

        >>> f = Functor(1)
        >>> print(f.map(lambda x: x + 1))
        2
        """
        return handle(self.value)

class FunctorIter(Generic[V]):
    """
    Stores an iterable value to be mapped by use of a handler function.

    value (attribute) Iterable[V]
      An iterable value provided for transformation via the map method.

    const (attribute) Any = None
      The constructor function corresponding to the value attribute type.

    pairs (attribute) Dict[str, Any] = {}
      A dictionary of keyword argument settings received at instantiation.

    map (method) handle: H, as_tree: bool = False -> Any
      Returns the instance value property once 'handle' has been applied
      to the whole by default or to each node if any 'as_tree' is truthy.
    """

    def __init__(self, value: Iterable[V], const: Any = None, **kwargs) -> None:
        """
        Returns a FunctorIter instance with a value property set to 'value',
        a const property set to 'const' or the constructor of 'value' and
        a pairs property set to the dictionary of keyword arguments

        >>> f = FunctorIter([1, [2, 3]])
        >>> print(f.__class__.__name__, f.value, f.const == list)
        FunctorIter [1, [2, 3]] True
        """
        self.value = value
        self.const = get_const(value) if const is None else const
        self.pairs = kwargs

    def map(self, handle: H, as_tree: bool = False) -> Any:
        """
        Returns the instance value property once 'handle' has been applied
        to the whole by default or to each node if any 'as_tree' is truthy.

        >>> f = FunctorIter([1, [2, 3]])
        >>> print(f.map(lambda x: x + 1, True))
        [2, [3, 4]]
        """
        if ('as_tree' in self.pairs and self.pairs['as_tree']) or as_tree:
            return traverse_iter(handle, self.value, self.const)
        return self.const(map(handle, self.value))

class FunctorDict(Generic[V]):
    """
    Stores a value of type dict to be mapped by use of a handler function.

    value (attribute) Dict[Any, V]
      A value of type dict provided for transformation via the map method.

    pairs (attribute) Dict[str, Any] = {}
      A dictionary of keyword argument settings received at instantiation.

    map (method) handle: H, as_tree: bool = False -> Any
      Returns the instance value property once 'handle' has been applied
      to the whole by default or to each node if any 'as_tree' is truthy.
    """

    def __init__(self, value: Dict[Any, V], **kwargs) -> None:
        """
        Returns a FunctorDict instance with a value property set to 'value'
        and a pairs property set to the dictionary of keyword arguments

        >>> f = FunctorDict({'a': 1, 'b': {'c': 2, 'd': 3}})
        >>> print(f.__class__.__name__, f.value)
        FunctorDict {'a': 1, 'b': {'c': 2, 'd': 3}}
        """
        self.value = value
        self.pairs = kwargs

    def map(self, handle: H, as_tree: bool = False) -> Any:
        """
        Returns the instance value property once 'handle' has been applied
        to the whole by default or to each node if any 'as_tree' is truthy.

        >>> f = FunctorDict({'a': 1, 'b': {'c': 2, 'd': 3}})
        >>> print(f.map(lambda x: x + 1, True))
        {'a': 2, 'b': {'c': 3, 'd': 4}}
        """
        if ('as_tree' in self.pairs and self.pairs['as_tree']) or as_tree:
            return traverse_dict(handle, self.value)
        return {k: handle(v) for k, v in self.value.items()}


# pointed functor classes

class PFunctor(Functor):
    """
    Stores a value of any type to be mapped by use of a handler function
    and returned in a new instance, allowing method calls to be chained.

    value (attribute) V
      A value of any type provided for transformation via the map method.

    of (class method) value: V -> Any
      Returns a PFunctor instance with a value property set to 'value'.

    map (method) handle: H -> Any
      Returns a new PFunctor instance with a value property being the
      previous instance value property once 'handle' has been applied.
    """

    @classmethod
    def of(cls, value: V) -> Any:
        """
        Returns a PFunctor instance with a value property set to 'value'.

        >>> pf = PFunctor.of(1)
        >>> print(pf.__class__.__name__, pf.value)
        PFunctor 1
        """
        return cls(value)

    def map(self, handle: H) -> Any:
        """
        Returns a new PFunctor instance with a value property being the
        previous instance value property once 'handle' has been applied.

        >>> pf = PFunctor(1)
        >>> print(pf.map(lambda x: x + 1).value)
        2
        """
        return self.of(handle(self.value))

class PFunctorIter(FunctorIter):
    """
    Stores an iterable value to be mapped by use of a handler function
    and returned in a new instance, allowing method calls to be chained.

    value (attribute) Iterable[V]
      An iterable value provided for transformation via the map method.

    const (attribute) Any = None
      The constructor function corresponding to the value attribute type.

    pairs (attribute) Dict[str, Any] = {}
      A dictionary of keyword argument settings received at instantiation.

    of (class method) value: Iterable[V], const: Any = None -> Any
      Returns a PFunctorIter instance with a value property set to 'value'
      and a const property set to 'const' or the constructor of 'value'.

    map (method) handle: H, as_tree: bool = False -> Any
      Returns a new PFunctorIter instance with a value property being the
      previous instance value property once 'handle' has been applied
      to the whole by default or to each node if any 'as_tree' is truthy.
    """

    @classmethod
    def of(cls, value: Iterable[V], const: Any = None, **kwargs) -> Any:
        """
        Returns a PFunctorIter instance with a value property set to 'value'
        a const property set to 'const' or the constructor of 'value' and
        a pairs property set to the dictionary of keyword arguments

        >>> pf = PFunctorIter([1, [2, 3]])
        >>> print(pf.__class__.__name__, pf.value, pf.const == list)
        PFunctorIter [1, [2, 3]] True
        """
        const = get_const(value) if const is None else const
        return cls(value, const, **kwargs)

    def map(self, handle: H, as_tree: bool = False) -> Any:
        """
        Returns a new PFunctorIter instance with a value property being the
        previous instance value property once 'handle' has been applied
        to the whole by default or to each node if any 'as_tree' is truthy.

        >>> pf = PFunctorIter([1, [2, 3]])
        >>> print(pf.map(lambda x: x + 1, True).value)
        [2, [3, 4]]
        """
        if ('as_tree' in self.pairs and self.pairs['as_tree']) or as_tree:
            traversed = traverse_iter(handle, self.value, self.const)
            return self.__class__(traversed)
        mapped = self.const(map(handle, self.value))
        return self.of(mapped)

class PFunctorDict(FunctorDict):
    """
    Stores a value of type dict to be mapped by use of a handler function
    and returned in a new instance, allowing method calls to be chained.

    value (attribute) Dict[Any, V]
      A value of type dict provided for transformation via the map method.

    pairs (attribute) Dict[str, Any] = {}
      A dictionary of keyword argument settings received at instantiation.

    of (class method) value: Dict[Any, V] -> Any
      Returns a PFunctorDict instance with a value property set to 'value'.

    map (method) handle: H, as_tree: bool = False -> Any
      Returns a new PFunctorDict instance with a value property being the
      previous instance value property once 'handle' has been applied
      to the whole by default or to each node if any 'as_tree' is truthy.
    """

    @classmethod
    def of(cls, value: Dict[Any, V], **kwargs) -> Any:
        """
        Returns a PFunctorDict instance with a value property set to 'value'
        and a pairs property set to the dictionary of keyword arguments

        >>> pf = PFunctorDict({'a': 1, 'b': {'c': 2, 'd': 3}})
        >>> print(pf.__class__.__name__, pf.value)
        PFunctorDict {'a': 1, 'b': {'c': 2, 'd': 3}}
        """
        return cls(value, **kwargs)

    def map(self, handle: H, as_tree: bool = False) -> Any:
        """
        Returns a new PFunctorDict instance with a value property being the
        previous instance value property once 'handle' has been applied
        to the whole by default or to each node if any 'as_tree' is truthy.

        >>> pf = PFunctorDict({'a': 1, 'b': {'c': 2, 'd': 3}})
        >>> print(pf.map(lambda x: x + 1, True).value)
        {'a': 2, 'b': {'c': 3, 'd': 4}}
        """
        if ('as_tree' in self.pairs and self.pairs['as_tree']) or as_tree:
            traversed = traverse_dict(handle, self.value)
            return self.__class__(traversed)
        mapped = {k: handle(v) for k, v in self.value.items()}
        return self.of(mapped)
