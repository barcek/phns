import unittest

from phns.factory import *


# test builders

get_test_build = lambda value, **kwargs: f'Test build properties: {value}, {kwargs}'


# test classes

class TestFactory(unittest.TestCase):

    def test_Factory(self):

        # instantiation

        instance = Phnew()
        self.assertEqual(instance.__class__, Phnew)

        # .register method

        instance.register('test_builder', get_test_build, {'is_test': True})
        self.assertEqual(instance.builders, {'test_builder': {'fn': get_test_build, 'kw': {'is_test': True}}})

        # __call__ built-in method

        test_build = instance('test_builder', 'test_value')
        self.assertEqual(test_build, "Test build properties: test_value, {'is_test': True}")

        # phnew

        self.assertEqual(phnew.__class__, Phnew)

        test_kw_f         = {'fn': get_functor, 'kw': {}}
        test_kw_f_as_is   = {'fn': get_functor, 'kw': {'as_is': True}}
        test_kw_f_as_tree = {'fn': get_functor, 'kw': {'as_tree': True}}

        self.assertEqual(phnew.builders['f.'],  test_kw_f_as_is)
        self.assertEqual(phnew.builders['f:'],  test_kw_f)
        self.assertEqual(phnew.builders['f:{'], test_kw_f_as_tree)
        self.assertEqual(phnew.builders['f'],   test_kw_f)
        self.assertEqual(phnew.builders['f{'],  test_kw_f_as_tree)

        test_kw_pf         = {'fn': get_pfunctor, 'kw': {}}
        test_kw_pf_as_is   = {'fn': get_pfunctor, 'kw': {'as_is': True}}
        test_kw_pf_as_tree = {'fn': get_pfunctor, 'kw': {'as_tree': True}}

        self.assertEqual(phnew.builders['pf.'],  test_kw_pf_as_is)
        self.assertEqual(phnew.builders['pf:'],  test_kw_pf)
        self.assertEqual(phnew.builders['pf:{'], test_kw_pf_as_tree)
        self.assertEqual(phnew.builders['pf'],   test_kw_pf)
        self.assertEqual(phnew.builders['pf{'],  test_kw_pf_as_tree)


if __name__ == '__main__':
    unittest.main()
