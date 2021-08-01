# phns

A typed and tested package stub with resources for functional programming in Python.

Currently implements base and pointed functor sets allowing recursive mapping of nested values, as well as the `curry`, `curry_n`, `compose` and `pipe` functions.

- [Using the resources](#using-the-resources)
    - [Base & pointed functors](#base--pointed-functors)
        - [Mapping](#mapping)
        - [Iterables](#iterables)
    - [Primary functions](#primary-functions)
        - [curry & curry_n](#curry--curry_n)
        - [compose & pipe](#compose--pipe)
    - [Utility functions](#utility-functions)
- [Tests, interactive examples & type checking](#tests-interactive-examples--type-checking)
- [Development plan](#development-plan)
- [Repository tree](#repository-tree)

## Using the resources

### Base & pointed functors

Import the `phnew` factory instance and pass the shorthand for the structure to be built along with its initial value. For a base functor, the shorthand is 'f', for a pointed functor 'pf'.

```python
from phns import phnew
demo_f = phnew('f', 1)
```

Alternatively, the given builder can be used independently:

```python
from phns.builder import get_functor
demo_f = get_functor(1)
```

A class can also be imported from `phns.functor` and instantiated directly, whether the base `Functor`, `FunctorIter` or `FunctorDict`, or the pointed `PFunctor`, `PFunctorIter` or `PFunctorDict`. For the `-Iter` classes, see [below](#iterable-values).

#### Mapping

Map by passing to the `.map` method the function to be applied to the internal value. The method return value is the result of the mapping. The internal value does not change.

```python
demo_f.map(lambda x: x + 1)
```

If the internal value is a `list`, `tuple` or `dict`, the second argument to `.map` can be set to `True` to apply the function not only to the data structure's top-level values, but also to nested instances.

With a pointed functor, the return value is a new instance of that functor, with the internal value being the result of the mapping. This allows uses of `.map` to be chained.

```python
PFunctor.of(1).map(lambda x: x + 1).map(lambda x: x * 2)
```

#### Iterables

The builder passes to `FunctorIter` and `PFunctorIter` only lists, tuples, sets, frozensets and bytearrays as the testing covers these types. For other iterables, instantiate direct, modifying if need be, or add the new type to the reference list in 'phns/builder.py'. Pull requests are welcome.

### Primary functions

For `curry`, `curry_n`, `compose` and `pipe`, import from 'phns/primary.py':

```python
from phns.primary import *
```

#### curry & curry_n

Passing an uncurried function to `curry` returns a collector function, allowing the initial function's arguments to be provided singly or in groups. The function is invoked when the last argument is received. The variation `curry_n` takes as its second argument an integer specifying the number of arguments to be collected.

#### compose & pipe

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

## Development plan

The following are the expected next steps in the development of the code base. The general medium-term aim is a comprehensive set of the core patterns applied in functional programming. Pull requests are welcome for these and other potential improvements.

- classes and builder for applicative functors, followed by a minimal base monad
- reducers and transducers

## Repository tree

```
./
├── phns
│   ├── __init__.py
│   ├── builder.py
│   ├── factory.py
│   ├── functor.py
│   ├── primary.py
│   └── utility.py
├── test
│   ├── __init__.py
│   ├── test_builder.py
│   ├── test_factory.py
│   ├── test_functor.py
│   ├── test_primary.py
│   └── test_utility.py
├── .gitignore
├── LICENSE.txt
├── README.md
├── requirements.txt
└── test.py
```
