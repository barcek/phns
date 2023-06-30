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
        self.assertEqual(int_built.value, value['int']['initial'])

        str_built = get_functor(value['str']['initial'])
        str_instantiated = Functor(value['str']['initial'])
        self.assertEqual(str_built.__class__, str_instantiated.__class__)
        self.assertEqual(str_built.value, value['str']['initial'])

        list_built = get_functor(value['list']['initial'], as_is=True)
        list_instantiated = Functor(value['list']['initial'])
        self.assertEqual(list_built.__class__, list_instantiated.__class__)
        self.assertEqual(list_built.value, value['list']['initial'])

        dict_built = get_functor(value['dict']['initial'], as_is=True)
        dict_instantiated = Functor(value['dict']['initial'])
        self.assertEqual(dict_built.__class__, dict_instantiated.__class__)
        self.assertEqual(dict_built.value, value['dict']['initial'])

        # FunctorIter

        list_built = get_functor(value['iter_list']['initial'])
        list_instantiated = FunctorIter(value['iter_list']['initial'])
        self.assertEqual(list_built.__class__, list_instantiated.__class__)
        self.assertEqual(list_built.value, value['iter_list']['initial'])

        list_built = get_functor(value['iter_list']['initial'], as_tree=True)
        list_instantiated = FunctorIter(value['iter_list']['initial'])
        self.assertEqual(list_built.__class__, list_instantiated.__class__)
        self.assertEqual(list_built.value, value['iter_list']['initial'])
        self.assertEqual(list_built.pairs['as_tree'], True)

        str_built = get_functor(value['str']['initial'], as_iter=True)
        str_instantiated = FunctorIter(value['str']['initial'])
        self.assertEqual(str_built.__class__, str_instantiated.__class__)
        self.assertEqual(str_built.value, value['str']['initial'])
        self.assertEqual(str_built.pairs['as_iter'], True)

        tuple_built = get_functor(value['iter_tuple']['initial'])
        tuple_instantiated = FunctorIter(value['iter_tuple']['initial'])
        self.assertEqual(tuple_built.__class__, tuple_instantiated.__class__)
        self.assertEqual(tuple_built.value, value['iter_tuple']['initial'])

        set_built = get_functor(value['iter_set']['initial'])
        set_instantiated = FunctorIter(value['iter_set']['initial'])
        self.assertEqual(set_built.__class__, set_instantiated.__class__)
        self.assertEqual(set_built.value, value['iter_set']['initial'])

        frozenset_built = get_functor(value['iter_frozenset']['initial'])
        frozenset_instantiated = FunctorIter(value['iter_frozenset']['initial'])
        self.assertEqual(frozenset_built.__class__, frozenset_instantiated.__class__)
        self.assertEqual(frozenset_built.value, value['iter_frozenset']['initial'])

        bytearray_built = get_functor(value['iter_bytearray']['initial'])
        bytearray_instantiated = FunctorIter(value['iter_bytearray']['initial'])
        self.assertEqual(bytearray_built.__class__, bytearray_instantiated.__class__)
        self.assertEqual(bytearray_built.value, value['iter_bytearray']['initial'])

        # FunctorDict

        dict_built = get_functor(value['dict_dict']['initial'])
        dict_instantiated = FunctorDict(value['dict_dict']['initial'])
        self.assertEqual(dict_built.__class__, dict_instantiated.__class__)
        self.assertEqual(dict_built.value, value['dict_dict']['initial'])

        dict_built = get_functor(value['dict_dict']['initial'], as_tree=True)
        dict_instantiated = FunctorDict(value['dict_dict']['initial'])
        self.assertEqual(dict_built.__class__, dict_instantiated.__class__)
        self.assertEqual(dict_built.value, value['dict_dict']['initial'])
        self.assertEqual(dict_built.pairs['as_tree'], True)

    def test_get_pfunctor(self):

        # PFunctor

        int_built = get_pfunctor(value['int']['initial'])
        int_lifted = PFunctor.of(value['int']['initial'])
        self.assertEqual(int_built.__class__, int_lifted.__class__)
        self.assertEqual(int_built.value, value['int']['initial'])

        str_built = get_pfunctor(value['str']['initial'])
        str_instantiated = PFunctor(value['str']['initial'])
        self.assertEqual(str_built.__class__, str_instantiated.__class__)
        self.assertEqual(str_built.value, value['str']['initial'])

        list_built = get_pfunctor(value['list']['initial'], as_is=True)
        list_lifted = PFunctor.of(value['list']['initial'])
        self.assertEqual(list_built.__class__, list_lifted.__class__)
        self.assertEqual(list_built.value, value['list']['initial'])

        dict_built = get_pfunctor(value['dict']['initial'], as_is=True)
        dict_lifted = PFunctor.of(value['dict']['initial'])
        self.assertEqual(dict_built.__class__, dict_lifted.__class__)
        self.assertEqual(dict_built.value, value['dict']['initial'])

        # PFunctorIter

        list_built = get_pfunctor(value['iter_list']['initial'])
        list_lifted = PFunctorIter.of(value['iter_list']['initial'])
        self.assertEqual(list_built.__class__, list_lifted.__class__)
        self.assertEqual(list_built.value, value['iter_list']['initial'])

        list_built = get_pfunctor(value['iter_list']['initial'], as_tree=True)
        list_lifted = PFunctorIter.of(value['iter_list']['initial'])
        self.assertEqual(list_built.__class__, list_lifted.__class__)
        self.assertEqual(list_built.value, value['iter_list']['initial'])
        self.assertEqual(list_built.pairs['as_tree'], True)

        str_built = get_pfunctor(value['str']['initial'], as_iter=True)
        str_instantiated = PFunctorIter(value['str']['initial'])
        self.assertEqual(str_built.__class__, str_instantiated.__class__)
        self.assertEqual(str_built.value, value['str']['initial'])
        self.assertEqual(str_built.pairs['as_iter'], True)

        tuple_built = get_pfunctor(value['iter_tuple']['initial'])
        tuple_lifted = PFunctorIter.of(value['iter_tuple']['initial'])
        self.assertEqual(tuple_built.__class__, tuple_lifted.__class__)
        self.assertEqual(tuple_built.value, value['iter_tuple']['initial'])

        set_built = get_pfunctor(value['iter_set']['initial'])
        set_lifted = PFunctorIter.of(value['iter_set']['initial'])
        self.assertEqual(set_built.__class__, set_lifted.__class__)
        self.assertEqual(set_built.value, value['iter_set']['initial'])

        frozenset_built = get_pfunctor(value['iter_frozenset']['initial'])
        frozenset_lifted = PFunctorIter.of(value['iter_frozenset']['initial'])
        self.assertEqual(frozenset_built.__class__, frozenset_lifted.__class__)
        self.assertEqual(frozenset_built.value, value['iter_frozenset']['initial'])

        bytearray_built = get_pfunctor(value['iter_bytearray']['initial'])
        bytearray_lifted = PFunctorIter.of(value['iter_bytearray']['initial'])
        self.assertEqual(bytearray_built.__class__, bytearray_lifted.__class__)
        self.assertEqual(bytearray_built.value, value['iter_bytearray']['initial'])

        # PFunctorDict

        dict_built = get_pfunctor(value['dict_dict']['initial'])
        dict_lifted = PFunctorDict.of(value['dict_dict']['initial'])
        self.assertEqual(dict_built.__class__, dict_lifted.__class__)
        self.assertEqual(dict_built.value, value['dict_dict']['initial'])

        dict_built = get_pfunctor(value['dict_dict']['initial'], as_tree=True)
        dict_lifted = PFunctorDict.of(value['dict_dict']['initial'])
        self.assertEqual(dict_built.__class__, dict_lifted.__class__)
        self.assertEqual(dict_built.value, value['dict_dict']['initial'])
        self.assertEqual(dict_built.pairs['as_tree'], True)


if __name__ == '__main__':
    unittest.main()
