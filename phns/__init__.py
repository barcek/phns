# phns v1.3.14
# ©2021 barcek
# License: MIT
# @ github.com
# /barcek/phns

"""
Resources to support a more functional style of programming,
incl. classes for base and pointed functors, a corresponding
builder set and related factory, and higher order functions:
- builder  builder functions returning instances of classes
- factory  a factory class and an instance for the builders
- functor  classes for variants of base and pointed functor
- primary  higher order functions both taking and returning
- utility  remaining higher order and first order functions
"""


from phns.factory import phnew as phnew
