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
    as_base = False if ('as_base' not in kwargs and 'as_is' not in kwargs)\
        else ('as_base' in kwargs and kwargs['as_base']) or kwargs['as_is']
    as_iter = False if 'as_iter' not in kwargs else kwargs['as_iter']
    if (not as_base and const in iterables_passed) or as_iter:
        return FunctorIter(value, const, **kwargs)
    if not as_base and const == dict:
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
    as_base = False if ('as_base' not in kwargs and 'as_is' not in kwargs)\
        else ('as_base' in kwargs and kwargs['as_base']) or kwargs['as_is']
    as_iter = False if 'as_iter' not in kwargs else kwargs['as_iter']
    if (not as_base and const in iterables_passed) or as_iter:
        return PFunctorIter.of(value, const, **kwargs)
    if not as_base and const == dict:
        return PFunctorDict.of(value, **kwargs)
    return PFunctor.of(value)
