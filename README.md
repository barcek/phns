# phns

A typed and tested package stub with resources for functional programming in Python.

Currently implements base and pointed functor sets allowing recursive mapping of nested values, as well as the `curry`, `curry_n`, `compose` and `pipe` functions.

- [Using the resources](#using-the-resources)
    - [Base & pointed functors](#base--pointed-functors)
        - [Mapping](#mapping)
        - [Containers](#containers)
          - [Nested mapping](#nested-mapping)
          - [Other iterables](#other-iterables)
        - [Shorthands](#shorthands)
          - [Base functors](#base-functors)
          - [Pointed functors](#pointed-functors)
    - [Primary functions](#primary-functions)
        - [curry & curry_n](#curry--curry_n)
        - [compose & pipe](#compose--pipe)
    - [Utility functions](#utility-functions)
- [Code verification](#code-verification)
  - [Type checking](#type-checking)
  - [Interactive examples](#interactive-examples)
  - [Unit tests](#unit-tests)
- [Development plan](#development-plan)
- [Repository tree](#repository-tree)

## Using the resources

Base and pointed functors can be used via the top-level `phnew` factory instance, as well as via the builders in 'phns/builder.py' and direct from 'phns/functor.py'.

The primary functions `curry`, `curry_n`, `compose` and `pipe` can be imported directly from 'phns/primary.py'.

Utility functions can be imported from 'phns/utility.py'.

### Base & pointed functors

Import the `phnew` factory instance and pass the shorthand for the structure to be built along with its initial internal value. For a base functor, the simplest shorthand is `f`, for a pointed functor `pf`.

```python
from phns import phnew
demo_f = phnew('f', 1)
```

Alternatively, the given builder can be used independently:

```python
from phns.builder import get_functor
demo_f = get_functor(1)
```

A class can also be imported from `phns.functor` and instantiated directly, whether the base `Functor`, `FunctorIter` or `FunctorDict`, or the pointed `PFunctor`, `PFunctorIter` or `PFunctorDict`.

Note that by default a list, tuple, set, frozenset or bytearray passed to the `phnew` factory instance or to a builder is added to an instance of the `-Iter` class, and a dictionary to an instance of the `-Dict` class. For more on these classes and overriding this behaviour, see [Containers](#containers) below.

For alternatives to `f` and `pf`, see [Shorthands](#shorthands) below.

#### Mapping

Each functor has a `.map` method for operations using its internal value. Map by passing to this method the function to be applied.

With a non-pointed functor, the return value of the method is the result of the mapping. The internal value does not change.

```python
demo_f.map(lambda x: x + 1)
```

With a pointed functor, the return value is a new instance of that functor, with its internal value being the result of the mapping. This allows uses of `.map` to be chained.

```python
PFunctor.of(1).map(lambda x: x + 1).map(lambda x: x * 2)
```

#### Containers

By default a list, tuple, set, frozenset or bytearray passed with the `phnew` `f` or `pf` shorthand or directly to a builder is added to an instance of the `-Iter` class, and a dictionary to an instance of the `-Dict` class. This means that each item in the data structure is mapped.

In order to avoid this and map the data structure as a whole, the `phnew` shorthand `f.` or `pf.` can be used:

```python
from phns import phnew
demo_f = phnew('f.', 1)
```

Alternatively, the given builder can have its `as_is` keyword argument set to `True`:

```python
from phns.builder import get_functor
demo_f = get_functor(1, as_is=True)
```

The corresponding `phnew` shorthands `f:` and `pf:` are equivalent to `f` and `pf`, providing the default behaviour. See also [Shorthands](#shorthands) below.

##### Nested mapping

In the case of either an `-Iter` instance containing a `list` or `tuple` or a `-Dict` instance, the mapping can be applied not only to the data structure's top-level values, but also to nested instances of the structure, by setting the `.map` method's second argument (`as_tree`) to `True`:

```python
FunctorIter([1, [2, 3]]).map(lambda x: x + 1, True)
```

An `-Iter` or `-Dict` instance also applies the function in this way if instantiated by whichever means with the `as_tree` keyword argument set to `True`:

```python
demo_fi_1 = get_functor([1, [2, 3]], as_tree=True)
demo_fi_2 = FunctorIter([1, [2, 3]], as_tree=True)
demo_pfi = PFunctorIter.of([1, [2, 3]], as_tree=True)
```

Alternatively, the appropriate `phnew` shorthand can be used, either `f:{` or `f{` for a base functor or `pf:{` or `pf{` for a pointed:

```python
demo_fi_3 = phnew('f:{', [1, 2, 3])
```

See also [Shorthands](#shorthands) below.

##### Other iterables

Note that the builders pass to the `-Iter` classes only lists, tuples, sets, frozensets and bytearrays as the testing covers these types. For other iterables, instantiate direct, modifying if need be, or add the new type to the reference list in 'phns/builder.py'. Pull requests are welcome.

#### Shorthands

##### Base functors

- `f` / `f:` builds based on value type, producing:
  - a `FunctorDict` if the value is a dictionary
  - a `FunctorIter` if the value is a list, tuple, set, frozenset or bytearray
  - a `Functor` otherwise

- `f{` / `f:{` builds based on value type and activates nested mapping, producing:
  - a `FunctorDict` if the value is a dictionary, with `as_tree` set to `True`
  - a `FunctorIter` if the value is a list, tuple, set, frozenset or bytearray, with `as_tree` set to `True`
  - a `Functor` otherwise

- `f.` builds irrespective of value type, producing a `Functor`

##### Pointed functors

- `pf` / `pf:` builds based on value type, producing:
  - a `PFunctorDict` if the value is a dictionary
  - a `PFunctorIter` if the value is a list, tuple, set, frozenset or bytearray
  - a `PFunctor` otherwise

- `pf{` / `pf:{` builds based on value type and activates nested mapping, producing:
  - a `PFunctorDict` if the value is a dictionary, with `as_tree` set to `True`
  - a `PFunctorIter` if the value is a list, tuple, set, frozenset or bytearray, with `as_tree` set to `True`
  - a `PFunctor` otherwise

- `pf.` builds irrespective of value type, producing a `PFunctor`

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

## Code verification

The two verification scripts - 'verify.py' and 'verify.sh' - can be used to check types and run the interactive examples and unit tests.

The verification scripts can be run as follows:

```shell
python3 verify.py
sh verify.sh
```

Either of the two can also be run with the command `./<filename>` while in the same directory, and from elsewhere using the pattern `path/to/<filename>`, by first making the file executable, if not already, with `chmod +x <filename>`. Both the Python and shell binary are assumed to be accessible via the '/usr/bin' directory, per the hashbang at the top of each file.

```shell
./verify.py
./verify.sh
```

Each of the three - type checking, interactive examples and unit tests - can instead be run individually using the specific command in 'verify.sh'.

### Type checking

Type checking uses Mypy, an external tool. The Mypy-related dependencies per Python 3.11 are listed in the file 'requirements.txt'.

To run the type checking only:

```shell
mypy phns/
```

### Interactive examples

The interactive examples use `doctest` in the standard library.

To run the interactive examples only:

```shell
python3 -m doctest phns/*.py
```

### Unit tests

The unit tests use `unittest`, also in the standard library.

To run the unit tests only:

```shell
python3 -m unittest --quiet test/*.py
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
├── verify.py
└── verify.sh
```
