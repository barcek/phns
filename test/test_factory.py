import unittest

from phns.factory import *


# test builders

get_test_build = lambda value: f'Test build value: {value}'


# test classes

class TestFactory(unittest.TestCase):

    def test_Factory(self):

        # instantiation

        instance = Phnew()
        self.assertEqual(instance.__class__, Phnew)

        # .register method

        instance.register('test_builder', get_test_build)
        self.assertEqual(instance.builders, {'test_builder': get_test_build})

        # __call__ built-in method

        test_build = instance('test_builder', 'test_value')
        self.assertEqual(test_build, 'Test build value: test_value')

        # phnew

        self.assertEqual(phnew.__class__, Phnew)
        self.assertEqual(list(phnew.builders.keys()), [
            'f',
            'pf'
        ])
        self.assertEqual(list(phnew.builders.values()), [
            get_functor,
            get_pfunctor
        ])


if __name__ == '__main__':
    unittest.main()
