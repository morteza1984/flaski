import unittest
import math_operations


class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(math_operations.add(3, 5), 8)
        self.assertEqual(math_operations.add(-1, 1), 0)
        self.assertEqual(math_operations.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(math_operations.subtract(10, 5), 5)
        self.assertEqual(math_operations.subtract(5, 10), -5)
        self.assertEqual(math_operations.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(math_operations.multiply(3, 4), 12)
        self.assertEqual(math_operations.multiply(-2, 3), -6)
        self.assertEqual(math_operations.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(math_operations.divide(10, 2), 5)
        self.assertEqual(math_operations.divide(5, 2), 2.5)
        self.assertAlmostEqual(
            math_operations.divide(1, 3), 0.3333333, places=6)

        with self.assertRaises(ValueError):
            math_operations.divide(5, 0)

    def test_power(self):
        self.assertEqual(math_operations.power(2, 3), 8)
        self.assertEqual(math_operations.power(5, 0), 1)
        self.assertEqual(math_operations.power(2, -1), 0.5)

    def test_sqrt(self):
        self.assertEqual(math_operations.sqrt(16), 4)
        self.assertEqual(math_operations.sqrt(0), 0)
        self.assertAlmostEqual(math_operations.sqrt(2), 1.41421356, places=6)

        with self.assertRaises(ValueError):
            math_operations.sqrt(-1)

    def test_is_prime(self):
        self.assertFalse(math_operations.is_prime(1))
        self.assertTrue(math_operations.is_prime(2))
        self.assertTrue(math_operations.is_prime(3))
        self.assertFalse(math_operations.is_prime(4))
        self.assertTrue(math_operations.is_prime(17))
        self.assertFalse(math_operations.is_prime(25))
        self.assertTrue(math_operations.is_prime(97))


if __name__ == '__main__':
    unittest.main()
