from typing import TypeVar, Union, Any

from phns.functor import Functor, FunctorIter, FunctorDict, PFunctor, PFunctorIter, PFunctorDict
from phns.utility import get_constructor


# builder functions

def get_functor(value: Any) -> Union[Functor, FunctorIter, FunctorDict]:
    const = get_constructor(value)
    if const in [list, tuple, set, frozenset, bytearray]:
        return FunctorIter(value, const)
    if const == dict:
        return FunctorDict(value)
    return Functor(value)

def get_pfunctor(value: Any) -> Union[PFunctor, PFunctorIter, PFunctorDict]:
    const = get_constructor(value)
    if const in [list, tuple, set, frozenset, bytearray]:
        return PFunctorIter.of(value, const)
    if const == dict:
        return PFunctorDict.of(value)
    return PFunctor.of(value)
