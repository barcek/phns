"""
Builder functions returning instances of the classes in 'phns/functor.py':
- get_functor   base functor classes (Functor, FunctorIter, FunctorDict)
- get_pfunctor  pointed functor classes (PFunctor, PFunctorIter, PFunctorDict)
"""


from typing import TypeVar, Union, Any

from phns.functor import Functor, FunctorIter, FunctorDict, PFunctor, PFunctorIter, PFunctorDict
from phns.utility import get_constructor


# builder values

iterables_passed = [list, tuple, set, frozenset, bytearray]


# builder functions

def get_functor(value: Any, **kwargs) -> Union[Functor, FunctorIter, FunctorDict]:
    """
    Returns a base functor instance with a value property set to 'value'
    of the class for either dictionary, other iterable or uniterable type,
    and, where passed, a const property set to the constructor of 'value'.

    >>> f = get_functor([1, 2, 3])
    >>> print(f.__class__.__name__, f.value, f.const == list)
    FunctorIter [1, 2, 3] True
    """
    const = get_constructor(value)
    as_is = False if 'as_is' not in kwargs else kwargs['as_is']
    if not as_is and const in iterables_passed:
        return FunctorIter(value, const, **kwargs)
    if not as_is and const == dict:
        return FunctorDict(value, **kwargs)
    return Functor(value)

def get_pfunctor(value: Any, **kwargs) -> Union[PFunctor, PFunctorIter, PFunctorDict]:
    """
    Returns a pointed functor instance with a value property set to 'value'
    of the class for either dictionary, other iterable or uniterable type,
    and, where passed, a const property set to the constructor of 'value'.

    >>> pf = get_pfunctor([1, 2, 3])
    >>> print(pf.__class__.__name__, pf.value, pf.const == list)
    PFunctorIter [1, 2, 3] True
    """
    const = get_constructor(value)
    as_is = False if 'as_is' not in kwargs else kwargs['as_is']
    if not as_is and const in iterables_passed:
        return PFunctorIter.of(value, const, **kwargs)
    if not as_is and const == dict:
        return PFunctorDict.of(value, **kwargs)
    return PFunctor.of(value)
