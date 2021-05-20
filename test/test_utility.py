import unittest

from phns.utility import *


# test values

apply = {

    'double': lambda x: x * 2
}

value = {

    'list_nested':

        {
            'initial': [1, [2, 2, [3, 3, 3]]],
            'doubled': [2, [4, 4, [6, 6, 6]]]
        },

    'tuple_nested':

        {
            'initial': (1, (2, 2, (3, 3, 3))),
            'doubled': (2, (4, 4, (6, 6, 6)))
        },

    'dict_nested':

        {
            'initial': {'a': 1, 'b': {'c': 2, 'd': 2, 'e': {'f': 3, 'g': 3, 'h': 3}}},
            'doubled': {'a': 2, 'b': {'c': 4, 'd': 4, 'e': {'f': 6, 'g': 6, 'h': 6}}}
        }
}


# test classes

class TestUtility(unittest.TestCase):

    # secondary functions

    def test_traverse_iter(self):

        list_doubled = traverse_iter(apply['double'], value['list_nested']['initial'])
        self.assertEqual(list_doubled, value['list_nested']['doubled'])

        tuple_doubled = traverse_iter(apply['double'], value['tuple_nested']['initial'], tuple)
        self.assertEqual(tuple_doubled, value['tuple_nested']['doubled'])

    def test_traverse_dict(self):

        dict_doubled = traverse_dict(apply['double'], value['dict_nested']['initial'])
        self.assertEqual(dict_doubled, value['dict_nested']['doubled'])

    def test_get_args(self):

        args = get_args(apply['double'])
        self.assertEqual(args, ['x'])

    # tertiary functions

    def test_get_constructor(self):

        int_constructor = get_constructor(1)
        self.assertEqual(int_constructor, int)

    def test_get_class_name(self):

        int_class_name = get_class_name(1)
        self.assertEqual(int_class_name, 'int')


if __name__ == '__main__':
    unittest.main()
