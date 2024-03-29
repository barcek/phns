"""
A factory class - Phnew - instantiated to register and call builder functions
and one instance - phnew - with the builders in 'phns/builder.py' registered,
returning when called directly instances of the classes in 'phns/functor.py'.
"""


from typing import TypeVar, Callable, Dict, Any

from phns.builder import get_functor, get_pfunctor


# types

P = TypeVar('P')
Builder = Callable[[P], Any]


# factory class

class Phnew():
    """
    Registers and acts as an interface to one or more builder functions.

    builders (attribute) Dict[str, Any] = {}
      Stores each builder registered to the instance keyed under its id.

    register (method) id: str, fn: Builder -> None
      Inserts builder 'fn' and its corresponding keyword dictionary 'kw'
      into the builders dictionary keyed under 'id'.

    __call__ (method) id: str, value: P -> Any
      Returns the result from the builder under 'id' when passed 'value'.
    """

    def __init__(self) -> None:
        """
        Returns an instance of Phnew with no builder functions registered.

        >>> p = Phnew()
        >>> print(p.__class__.__name__, p.builders)
        Phnew {}
        """
        self.builders: Dict[str, Any] = {}

    def register(self, id: str, fn: Builder, kw: Dict = {}) -> None:
        """
        Inserts builder 'fn' into the builders dictionary keyed under 'id'.

        >>> p = Phnew()
        >>> p.register('get_int', lambda x: int(x))
        >>> p.builders['get_int']['fn'](1)
        1
        """
        self.builders[id] = {'fn': fn, 'kw': kw};

    def __call__(self, id: str, value: P) -> Any:
        """
        Returns the result from the builder under 'id' when passed 'value'.

        >>> p = Phnew()
        >>> p.register('get_int', lambda x: int(x))
        >>> p('get_int', 1)
        1
        """
        if id in self.builders:
            return self.builders[id]['fn'](value, **self.builders[id]['kw'])
        raise ValueError(id)


# factory instantiation & builder registration

phnew = Phnew()

# - functors
phnew.register('f.',  get_functor, {'as_base': True})
phnew.register('f:',  get_functor)
phnew.register('f:.', get_functor, {'as_iter': True})
phnew.register('f:{', get_functor, {'as_tree': True})
phnew.register('f',   get_functor)
phnew.register('f{',  get_functor, {'as_tree': True})

# - pointed functors
phnew.register('pf.',  get_pfunctor, {'as_base': True})
phnew.register('pf:',  get_pfunctor)
phnew.register('pf:.', get_pfunctor, {'as_iter': True})
phnew.register('pf:{', get_pfunctor, {'as_tree': True})
phnew.register('pf',   get_pfunctor)
phnew.register('pf{',  get_pfunctor, {'as_tree': True})
