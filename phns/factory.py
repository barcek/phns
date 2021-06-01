from typing import TypeVar, Callable, Dict, Any

from phns.builder import get_functor, get_pfunctor


# types

P = TypeVar('P')
Builder = Callable[[P], Any]


# factory class

class Phnew():

    def __init__(self):
        """Returns an instance of Phnew with an empty builders dictionary.
           >>> p = Phnew()
           >>> print(p.__class__.__name__, p.builders)
           Phnew {}
        """
        self.builders: Dict[str, Any] = {}

    def register(self, id: str, fn: Builder) -> None:
        """Adds builder 'fn' to the builders dictionary keyed under 'id'.
           >>> p = Phnew()
           >>> p.register('get_int', lambda x: int(x))
           >>> p.builders['get_int'](1)
           1
        """
        self.builders[id] = fn;

    def __call__(self, id: str, value: P) -> Any:
        """Returns the result from the builder at 'id' when passed 'value'.
           >>> p = Phnew()
           >>> p.register('get_int', lambda x: int(x))
           >>> p('get_int', 1)
           1
        """
        if id in self.builders:
            return self.builders[id](value)
        raise ValueError(id)


# factory instantiation & builder registration

phnew = Phnew()
phnew.register('f', get_functor)
phnew.register('pf', get_pfunctor)
