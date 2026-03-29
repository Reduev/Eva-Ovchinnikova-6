import unittest
import sys

def factorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result


class TestFactorial(unittest.TestCase):

    def test_positive_number(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(1), 1)

    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_negative_number(self):
        with self.assertRaises(ValueError) as context:
            factorial(-1)
        self.assertEqual(str(context.exception), "Факториал отрицательного числа не определен")

    def test_large_number_overflow(self):
        with self.assertRaises(ValueError) as context:
            factorial(1000)
        self.assertIn("не поддерживается типом int", str(context.exception))

    def test_boundary_case_one(self):
        self.assertEqual(factorial(1), 1)

    def test_sequence_of_values(self):
        test_cases = [(2, 2), (4, 24), (6, 720)]
        for n, expected in test_cases:
            with self.subTest(n=n):
                self.assertEqual(factorial(n), expected)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            factorial(3.5)

if __name__ == '__main__':
    unittest.main()