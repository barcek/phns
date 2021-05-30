import unittest

from phns.builder import *


# test values

from test.test_functor import value


# test classes

class TestBuilder(unittest.TestCase):

    def test_get_functor(self):

        # Functor

        int_built = get_functor(value['int']['initial'])
        int_instantiated = Functor(value['int']['initial'])
        self.assertEqual(int_built.__class__, int_instantiated.__class__)
        self.assertEqual(int_instantiated.value, value['int']['initial'])

        # FunctorIter

        list_built = get_functor(value['list']['initial'])
        list_instantiated = FunctorIter(value['list']['initial'])
        self.assertEqual(list_built.__class__, list_instantiated.__class__)
        self.assertEqual(list_instantiated.value, value['list']['initial'])

        tuple_built = get_functor(value['tuple']['initial'])
        tuple_instantiated = FunctorIter(value['tuple']['initial'])
        self.assertEqual(tuple_built.__class__, tuple_instantiated.__class__)
        self.assertEqual(tuple_instantiated.value, value['tuple']['initial'])

        set_built = get_functor(value['set']['initial'])
        set_instantiated = FunctorIter(value['set']['initial'])
        self.assertEqual(set_built.__class__, set_instantiated.__class__)
        self.assertEqual(set_instantiated.value, value['set']['initial'])

        frozenset_built = get_functor(value['frozenset']['initial'])
        frozenset_instantiated = FunctorIter(value['frozenset']['initial'])
        self.assertEqual(frozenset_built.__class__, frozenset_instantiated.__class__)
        self.assertEqual(frozenset_instantiated.value, value['frozenset']['initial'])

        bytearray_built = get_functor(value['bytearray']['initial'])
        bytearray_instantiated = FunctorIter(value['bytearray']['initial'])
        self.assertEqual(bytearray_built.__class__, bytearray_instantiated.__class__)
        self.assertEqual(bytearray_instantiated.value, value['bytearray']['initial'])

        # FunctorDict

        dict_built = get_functor(value['dict']['initial'])
        dict_instantiated = FunctorDict(value['dict']['initial'])
        self.assertEqual(dict_built.__class__, dict_instantiated.__class__)
        self.assertEqual(dict_instantiated.value, value['dict']['initial'])

    def test_get_pfunctor(self):

        # PFunctor

        int_built = get_pfunctor(value['int']['initial'])
        int_lifted = PFunctor.of(value['int']['initial'])
        self.assertEqual(int_built.__class__, int_lifted.__class__)
        self.assertEqual(int_lifted.value, value['int']['initial'])

        # PFunctorIter

        list_built = get_pfunctor(value['list']['initial'])
        list_lifted = PFunctorIter.of(value['list']['initial'])
        self.assertEqual(list_built.__class__, list_lifted.__class__)
        self.assertEqual(list_lifted.value, value['list']['initial'])

        tuple_built = get_pfunctor(value['tuple']['initial'])
        tuple_lifted = PFunctorIter.of(value['tuple']['initial'])
        self.assertEqual(tuple_built.__class__, tuple_lifted.__class__)
        self.assertEqual(tuple_lifted.value, value['tuple']['initial'])

        set_built = get_pfunctor(value['set']['initial'])
        set_lifted = PFunctorIter.of(value['set']['initial'])
        self.assertEqual(set_built.__class__, set_lifted.__class__)
        self.assertEqual(set_lifted.value, value['set']['initial'])

        frozenset_built = get_pfunctor(value['frozenset']['initial'])
        frozenset_lifted = PFunctorIter.of(value['frozenset']['initial'])
        self.assertEqual(frozenset_built.__class__, frozenset_lifted.__class__)
        self.assertEqual(frozenset_lifted.value, value['frozenset']['initial'])

        bytearray_built = get_pfunctor(value['bytearray']['initial'])
        bytearray_lifted = PFunctorIter.of(value['bytearray']['initial'])
        self.assertEqual(bytearray_built.__class__, bytearray_lifted.__class__)
        self.assertEqual(bytearray_lifted.value, value['bytearray']['initial'])

        # PFunctorDict

        dict_built = get_pfunctor(value['dict']['initial'])
        dict_lifted = PFunctorDict.of(value['dict']['initial'])
        self.assertEqual(dict_built.__class__, dict_lifted.__class__)
        self.assertEqual(dict_lifted.value, value['dict']['initial'])


if __name__ == '__main__':
    unittest.main()
