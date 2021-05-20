import unittest

from phns.primary import *


# test_values

apply = {

    'sum_2': lambda x, y: x + y,
    'sum_3': lambda x, y, z: x + y + z,

    'incr_1': lambda x: x + 1,
    'double': lambda x: x * 2,
    'square': lambda x: x * x
}


# test classes

class TestPrimary(unittest.TestCase):

    def test_curry(self):

        curried_sum2 = curry(apply['sum_2'])
        curried_sum3 = curry(apply['sum_3'])

        curried_sum3_1 = curried_sum3(1)

        self.assertEqual(curried_sum2(1)(2), 3)

        self.assertEqual(curried_sum3(1, 2, 3), 6)
        self.assertEqual(curried_sum3(1, 2)(3), 6)
        self.assertEqual(curried_sum3(1)(2)(3), 6)

    def test_compose(self):

        process = compose(apply['incr_1'])
        processed = process(1)
        self.assertEqual(processed, 2)

        process = compose(apply['incr_1'], apply['double'], apply['square'])
        processed = process(1)
        self.assertEqual(processed, 3)

        process = compose(apply['incr_1'], apply['double'], apply['square'], apply['sum_3'])
        processed = process(1, 2, 3)
        self.assertEqual(processed, 73)

    def test_pipe(self):

        process = pipe(apply['incr_1'])
        processed = process(1)
        self.assertEqual(processed, 2)

        process = pipe(apply['incr_1'], apply['double'], apply['square'])
        processed = process(1)
        self.assertEqual(processed, 16)

        process = pipe(apply['sum_3'], apply['incr_1'], apply['double'], apply['square'])
        processed = process(1, 2, 3)
        self.assertEqual(processed, 196)


if __name__ == '__main__':
    unittest.main()
