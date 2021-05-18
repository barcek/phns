import unittest

from phns.functor import *


# test values

apply = {

    'list_3': lambda x: [x, x, x],
    'double': lambda x: x * 2,
    'asc_32': lambda x: 32
}

value = {

    'int':

        {
            'initial':      1,
            'list3ed':      [1, 1, 1]
        },

    'list':

        {
            'initial':      [1, [2, 3]],
            'list3ed':      [[1, 1, 1], [[2, 3], [2, 3], [2, 3]]],
            'list3ed_tree': [[1, 1, 1], [[2, 2, 2], [3, 3, 3]]]
        },

    'tuple':

        {
            'initial':      (1, (2, 3)),
            'list3ed':      ([1, 1, 1], [(2, 3), (2, 3), (2, 3)]),
            'list3ed_tree': ([1, 1, 1], ([2, 2, 2], [3, 3, 3]))
        },

    'set':

        {
            'initial':      {1, 2},
            'doubled':      {2, 4}
        },

    'frozenset':

        {
            'initial':      frozenset([1, 2]),
            'doubled':      frozenset({2, 4})
        },

    'bytearray':

        {
            'initial':      bytearray('test_value', encoding='utf-8'),
            'asc32ed':      bytearray(b'          ')
        },

    'dict':

        {
            'initial':      {'a': 1, 'b': {'c': 2, 'd': 3}},
            'list3ed':      {'a': [1, 1, 1], 'b': [{'c': 2, 'd': 3}, {'c': 2, 'd': 3}, {'c': 2, 'd': 3}]},
            'list3ed_tree': {'a': [1, 1, 1], 'b': {'c': [2, 2, 2], 'd': [3, 3, 3]}}
        }
}


# test classes

class TestFunctor(unittest.TestCase):

    # instantiation / .value property

    def test_Functor(self):

        int_instantiated = Functor(value['int']['initial'])
        self.assertEqual(int_instantiated.value, value['int']['initial'])

    def test_FunctorIter(self):

        list_instantiated = FunctorIter(value['list']['initial'])
        self.assertEqual(list_instantiated.value, value['list']['initial'])

    def test_FunctorDict(self):

        dict_instantiated = FunctorDict(value['dict']['initial'])
        self.assertEqual(dict_instantiated.value, value['dict']['initial'])

    # .map method

    # - on Functor

    def test_Functor_map(self):

        int_list3ed = Functor(value['int']['initial']).map(apply['list_3'])
        self.assertEqual(int_list3ed, value['int']['list3ed'])

    # - on FunctorIter w/ list, tuple, set

    def test_FunctorIter_map(self):

        list_list3ed = FunctorIter(value['list']['initial']).map(apply['list_3'])
        self.assertEqual(list_list3ed, value['list']['list3ed'])

        tuple_list3ed = FunctorIter(value['tuple']['initial']).map(apply['list_3'])
        self.assertEqual(tuple_list3ed, value['tuple']['list3ed'])

        set_doubled = FunctorIter(value['set']['initial']).map(apply['double'])
        self.assertEqual(set_doubled, value['set']['doubled'])

        frozenset_doubled = FunctorIter(value['frozenset']['initial']).map(apply['double'])
        self.assertEqual(frozenset_doubled, value['frozenset']['doubled'])

        bytearray_asc32ed = FunctorIter(value['bytearray']['initial']).map(apply['asc_32'])
        self.assertEqual(bytearray_asc32ed, value['bytearray']['asc32ed'])

    def test_FunctorIter_map_as_tree(self):

        list_list3ed_tree = FunctorIter(value['list']['initial']).map(apply['list_3'], True)
        self.assertEqual(list_list3ed_tree, value['list']['list3ed_tree'])

        tuple_list3ed_tree = FunctorIter(value['tuple']['initial']).map(apply['list_3'], True)
        self.assertEqual(tuple_list3ed_tree, value['tuple']['list3ed_tree'])

        # set & frozenset unhashable & bytearray uninterpretable - no nesting

    # - on FunctorDict

    def test_FunctorDict_map(self):

        dict_list3ed = FunctorDict(value['dict']['initial']).map(apply['list_3'])
        self.assertEqual(dict_list3ed, value['dict']['list3ed'])

    def test_FunctorDict_map_as_tree(self):

        dict_list3ed_tree = FunctorDict(value['dict']['initial']).map(apply['list_3'], True)
        self.assertEqual(dict_list3ed_tree, value['dict']['list3ed_tree'])


if __name__ == '__main__':
    unittest.main()
