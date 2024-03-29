import unittest

from phns.functor import *


# test values

apply = {

    'list_3': lambda x: [x, x, x],
    'double': lambda x: x * 2,
    'tab_l1': lambda x: f'\t{x}',
    'asc_32': lambda x: 32
}

value = {

    'int': {
        'initial':      1,
        'list3ed':      [1, 1, 1]
    },

    'str': {
        'initial':      'abc',
        'tabl1ed':      '\tabc'
    },

    'list': {
        'initial':      [1, [2, 3]],
        'list3ed':      [[1, [2, 3]], [1, [2, 3]], [1, [2, 3]]]
    },

    'dict': {
        'initial':      {'a': 1, 'b': {'c': 2, 'd': 3}},
        'list3ed':      [{'a': 1, 'b': {'c': 2, 'd': 3}}, {'a': 1, 'b': {'c': 2, 'd': 3}}, {'a': 1, 'b': {'c': 2, 'd': 3}}]
    },

    'iter_str': {

        'initial':      'abc',
        'tabl1ed':      '\ta\tb\tc'
    },

    'iter_list': {

        'initial':      [1, [2, 3]],
        'list3ed':      [[1, 1, 1], [[2, 3], [2, 3], [2, 3]]],
        'list3ed_tree': [[1, 1, 1], [[2, 2, 2], [3, 3, 3]]]
    },

    'iter_tuple': {

        'initial':      (1, (2, 3)),
        'list3ed':      ([1, 1, 1], [(2, 3), (2, 3), (2, 3)]),
        'list3ed_tree': ([1, 1, 1], ([2, 2, 2], [3, 3, 3]))
    },

    'iter_set': {

        'initial':      {1, 2},
        'doubled':      {2, 4}
    },

    'iter_frozenset': {

        'initial':      frozenset([1, 2]),
        'doubled':      frozenset({2, 4})
    },

    'iter_bytearray': {

        'initial':      bytearray('test_value', encoding='utf-8'),
        'asc32ed':      bytearray(b'          ')
    },

    'dict_dict': {

        'initial':      {'a': 1, 'b': {'c': 2, 'd': 3}},
        'list3ed':      {'a': [1, 1, 1], 'b': [{'c': 2, 'd': 3}, {'c': 2, 'd': 3}, {'c': 2, 'd': 3}]},
        'list3ed_tree': {'a': [1, 1, 1], 'b': {'c': [2, 2, 2], 'd': [3, 3, 3]}}
    }
}


# test classes

class TestFunctorBase(unittest.TestCase):

    # instantiation / .value, .pairs properties

    def test_Functor(self):

        int_instantiated = Functor(value['int']['initial'])
        self.assertEqual(int_instantiated.value, value['int']['initial'])

        str_instantiated = Functor(value['str']['initial'])
        self.assertEqual(str_instantiated.value, value['str']['initial'])

    def test_FunctorIter(self):

        str_instantiated = FunctorIter(value['iter_str']['initial'])
        self.assertEqual(str_instantiated.value, value['iter_str']['initial'])

        list_instantiated = FunctorIter(value['iter_list']['initial'])
        self.assertEqual(list_instantiated.value, value['iter_list']['initial'])

        list_instantiated_tree = FunctorIter(value['iter_list']['initial'], as_tree=True)
        self.assertEqual(list_instantiated_tree.pairs['as_tree'], True)

    def test_FunctorDict(self):

        dict_instantiated = FunctorDict(value['dict_dict']['initial'])
        self.assertEqual(dict_instantiated.value, value['dict_dict']['initial'])

        dict_instantiated_tree = FunctorDict(value['dict_dict']['initial'], as_tree=True)
        self.assertEqual(dict_instantiated_tree.pairs['as_tree'], True)

    # .map method

    # - on Functor

    def test_Functor_map(self):

        int_list3ed = Functor(value['int']['initial']).map(apply['list_3'])
        self.assertEqual(int_list3ed, value['int']['list3ed'])

        str_tabl1ed = Functor(value['str']['initial']).map(apply['tab_l1'])
        self.assertEqual(str_tabl1ed, value['str']['tabl1ed'])

        list_list3ed = Functor(value['list']['initial']).map(apply['list_3'])
        self.assertEqual(list_list3ed, value['list']['list3ed'])

        dict_list3ed = Functor(value['dict']['initial']).map(apply['list_3'])
        self.assertEqual(dict_list3ed, value['dict']['list3ed'])

    # - on FunctorIter w/ list, tuple, set

    def test_FunctorIter_map(self):

        str_tabl1ed = FunctorIter(value['iter_str']['initial']).map(apply['tab_l1'])
        self.assertEqual(str_tabl1ed, value['iter_str']['tabl1ed'])

        list_list3ed = FunctorIter(value['iter_list']['initial']).map(apply['list_3'])
        self.assertEqual(list_list3ed, value['iter_list']['list3ed'])

        tuple_list3ed = FunctorIter(value['iter_tuple']['initial']).map(apply['list_3'])
        self.assertEqual(tuple_list3ed, value['iter_tuple']['list3ed'])

        set_doubled = FunctorIter(value['iter_set']['initial']).map(apply['double'])
        self.assertEqual(set_doubled, value['iter_set']['doubled'])

        frozenset_doubled = FunctorIter(value['iter_frozenset']['initial']).map(apply['double'])
        self.assertEqual(frozenset_doubled, value['iter_frozenset']['doubled'])

        bytearray_asc32ed = FunctorIter(value['iter_bytearray']['initial']).map(apply['asc_32'])
        self.assertEqual(bytearray_asc32ed, value['iter_bytearray']['asc32ed'])

    def test_FunctorIter_map_as_tree(self):

        list_list3ed_tree = FunctorIter(value['iter_list']['initial']).map(apply['list_3'], True)
        self.assertEqual(list_list3ed_tree, value['iter_list']['list3ed_tree'])

        list_list3ed_tree = FunctorIter(value['iter_list']['initial'], as_tree=True).map(apply['list_3'])
        self.assertEqual(list_list3ed_tree, value['iter_list']['list3ed_tree'])

        tuple_list3ed_tree = FunctorIter(value['iter_tuple']['initial']).map(apply['list_3'], True)
        self.assertEqual(tuple_list3ed_tree, value['iter_tuple']['list3ed_tree'])

        # set & frozenset unhashable & bytearray uninterpretable - no nesting

    # - on FunctorDict

    def test_FunctorDict_map(self):

        dict_list3ed = FunctorDict(value['dict_dict']['initial']).map(apply['list_3'])
        self.assertEqual(dict_list3ed, value['dict_dict']['list3ed'])

    def test_FunctorDict_map_as_tree(self):

        dict_list3ed_tree = FunctorDict(value['dict_dict']['initial']).map(apply['list_3'], True)
        self.assertEqual(dict_list3ed_tree, value['dict_dict']['list3ed_tree'])

        dict_list3ed_tree = FunctorDict(value['dict_dict']['initial'], as_tree=True).map(apply['list_3'])
        self.assertEqual(dict_list3ed_tree, value['dict_dict']['list3ed_tree'])


class TestFunctorPointed(unittest.TestCase):

    # instantiation / .value, .pairs properties

    def test_PFunctor(self):

        int_instantiated = PFunctor(value['int']['initial'])
        self.assertEqual(int_instantiated.value, value['int']['initial'])

        str_instantiated = PFunctor(value['str']['initial'])
        self.assertEqual(str_instantiated.value, value['str']['initial'])

    def test_PFunctorIter(self):

        str_instantiated = PFunctorIter(value['iter_str']['initial'])
        self.assertEqual(str_instantiated.value, value['iter_str']['initial'])

        list_instantiated = PFunctorIter(value['iter_list']['initial'])
        self.assertEqual(list_instantiated.value, value['iter_list']['initial'])

        list_instantiated_tree = PFunctorIter(value['iter_list']['initial'], as_tree=True)
        self.assertEqual(list_instantiated_tree.pairs['as_tree'], True)

    def test_PFunctorDict(self):

        dict_instantiated = PFunctorDict(value['dict_dict']['initial'])
        self.assertEqual(dict_instantiated.value, value['dict_dict']['initial'])

        dict_instantiated_tree = PFunctorDict(value['dict_dict']['initial'], as_tree=True)
        self.assertEqual(dict_instantiated_tree.pairs['as_tree'], True)

    # .of class method

    def test_PFunctor_of(self):

        int_lifted = PFunctor.of(value['int']['initial'])
        self.assertEqual(int_lifted.value, value['int']['initial'])

        str_lifted = PFunctor.of(value['str']['initial'])
        self.assertEqual(str_lifted.value, value['str']['initial'])

        list_lifted = PFunctor.of(value['list']['initial'])
        self.assertEqual(list_lifted.value, value['list']['initial'])

        dict_lifted = PFunctor.of(value['dict']['initial'])
        self.assertEqual(dict_lifted.value, value['dict']['initial'])

    def test_PFunctorIter_of(self):

        str_lifted = PFunctorIter.of(value['iter_str']['initial'])
        self.assertEqual(str_lifted.value, value['iter_str']['initial'])

        list_lifted = PFunctorIter.of(value['iter_list']['initial'])
        self.assertEqual(list_lifted.value, value['iter_list']['initial'])

        list_lifted_tree = PFunctorIter.of(value['iter_list']['initial'], as_tree=True)
        self.assertEqual(list_lifted_tree.pairs['as_tree'], True)

    def test_PFunctorDict_of(self):

        dict_lifted = PFunctorIter.of(value['dict_dict']['initial'])
        self.assertEqual(dict_lifted.value, value['dict_dict']['initial'])

        dict_lifted_tree = PFunctorIter.of(value['dict_dict']['initial'], as_tree=True)
        self.assertEqual(dict_lifted_tree.pairs['as_tree'], True)

    # .map method

    # - on PFunctor

    def test_PFunctor_map(self):

        str_tabl1ed = PFunctor.of(value['str']['initial']).map(apply['tab_l1'])
        self.assertEqual(str_tabl1ed.value, value['str']['tabl1ed'])

        int_list3ed = PFunctor.of(value['int']['initial']).map(apply['list_3'])
        self.assertEqual(int_list3ed.value, value['int']['list3ed'])

        list_list3ed = PFunctor.of(value['list']['initial']).map(apply['list_3'])
        self.assertEqual(list_list3ed.value, value['list']['list3ed'])

        dict_list3ed = PFunctor.of(value['dict']['initial']).map(apply['list_3'])
        self.assertEqual(dict_list3ed.value, value['dict']['list3ed'])

    # - on PFunctorIter w/ list, tuple, set

    def test_PFunctorIter_map(self):

        str_tabl1ed = PFunctorIter.of(value['iter_str']['initial']).map(apply['tab_l1'])
        self.assertEqual(str_tabl1ed.value, value['iter_str']['tabl1ed'])

        list_list3ed = PFunctorIter.of(value['iter_list']['initial']).map(apply['list_3'])
        self.assertEqual(list_list3ed.value, value['iter_list']['list3ed'])

        tuple_list3ed = PFunctorIter.of(value['iter_tuple']['initial']).map(apply['list_3'])
        self.assertEqual(tuple_list3ed.value, value['iter_tuple']['list3ed'])

        set_list3ed = PFunctorIter.of(value['iter_set']['initial']).map(apply['double'])
        self.assertEqual(set_list3ed.value, value['iter_set']['doubled'])

    def test_PFunctorIter_map_as_tree(self):

        list_list3ed_tree = PFunctorIter.of(value['iter_list']['initial']).map(apply['list_3'], True)
        self.assertEqual(list_list3ed_tree.value, value['iter_list']['list3ed_tree'])

        list_list3ed_tree = PFunctorIter.of(value['iter_list']['initial'], as_tree=True).map(apply['list_3'])
        self.assertEqual(list_list3ed_tree.value, value['iter_list']['list3ed_tree'])

        tuple_list3ed_tree = PFunctorIter.of(value['iter_tuple']['initial']).map(apply['list_3'], True)
        self.assertEqual(tuple_list3ed_tree.value, value['iter_tuple']['list3ed_tree'])

        # set unhashable - no nesting

    def test_PFunctorDict_map(self):

        dict_list3ed = PFunctorDict.of(value['dict_dict']['initial']).map(apply['list_3'])
        self.assertEqual(dict_list3ed.value, value['dict_dict']['list3ed'])

    def test_PFunctorDict_map_as_tree(self):

        dict_list3ed_tree = PFunctorDict.of(value['dict_dict']['initial']).map(apply['list_3'], True)
        self.assertEqual(dict_list3ed_tree.value, value['dict_dict']['list3ed_tree'])

        dict_list3ed_tree = PFunctorDict.of(value['dict_dict']['initial'], as_tree=True).map(apply['list_3'])
        self.assertEqual(dict_list3ed_tree.value, value['dict_dict']['list3ed_tree'])


if __name__ == '__main__':
    unittest.main()
