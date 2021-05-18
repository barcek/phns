from typing import TypeVar, Callable, Dict, Any

from phns.builder import get_functor


# types

P = TypeVar('P')
Builder = Callable[[P], Any]


# factory class

class Phnew():

    def __init__(self):
        self.builders: Dict[str, Any] = {}

    def register(self, id: str, fn: Builder) -> None:
        self.builders[id] = fn;

    def __call__(self, id: str, value: P) -> Any:
        if id in self.builders:
            return self.builders[id](value)
        raise ValueError(id)


# factory instantiation & builder registration

phnew = Phnew()
phnew.register('f', get_functor)
