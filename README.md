# phns

A typed and tested package stub with resources for functional programming in Python.

Currently implements a minimal base functor set allowing recursive mapping of nested values, as well as the `curry`, `curry_n`, `compose` and `pipe` functions.

## Use

### Base functors

Import the `phnew` factory instance and pass the shorthand for the structure to be built along with its initial value. For a base functor, the shorthand is 'f'.

```python
from phns import phnew
demo = phnew('f', 1)
```

Alternatively, the specific builder can be used directly:

```python
from phns.builder import get_functor
demo = get_functor(1)
```

Or instantiate `Functor`, `FunctorIter` or `FunctorDict` imported from `phns.functor`. If `FunctorIter`, see [below](#functors--iterables).

Map by passing to the `.map` method the function to be applied to the internal value.

If the value is a `list`, `tuple` or `dict`, the second argument to `.map` can be set to `True` to apply the function not only to the data structure's top-level values, but also to nested instances.

#### Functors & iterables

The builder passes to `FunctorIter` only lists, tuples, sets, frozensets and bytearrays as the testing covers these types. For other iterables, instantiate direct, modifying if need be, or add the new type to the reference list in 'phns/builder.py'. Pull requests are welcome.

### Primary functions

For `curry`, `curry_n`, `compose` and `pipe`, import from 'phns/primary.py':

```python
from phns.primary import *
```

Passing an uncurried function to `curry` returns a collector function, allowing the initial function's arguments to be provided singly or in groups. The function is invoked when the last argument is received. The variation `curry_n` takes as its second argument an integer specifying the number of arguments to be collected.

Passing one or more functions to `compose` or `pipe` returns a single function to call the whole set in sequence. The process begins when this is called with any arguments to the first in the set, with the return value from each passed to the next, or out from the last. Note that `compose` calls the set from right to left, `pipe` from left to right.

### Utility functions

The module 'phns/utility.py' includes `traverse_iter` and `traverse_dict` for trees of a given data structure, plus `get_args` to help determine arity.

## Tests, interactive examples & type checking

Run the file 'test.py' to check types and run the interactive examples and unit tests. Type checking uses the Mypy package, while the examples are run with `doctest` and the fuller tests with `unittest`, both in the standard library.

```shell
python3 test.py
```

To run the type checking only:

```shell
mypy phns/
```

Just the interactive examples:

```shell
python3 -m doctest phns/*.py
```

For testing alone:

```shell
python3 -m unittest discover test
```

## Next

- docstrings and examples
- classes and builders for pointed and applicative functors, followed by a minimal base monad
