import unittest
import add_digits


class TestAddDigits(unittest.TestCase):

    def test_sum_number_digits(self):
        # Test single digits
        for i in range(10):
            self.assertEqual(add_digits.sum_number_digits(i), i)

        # Test numbers with one pass
        cases = ((13, 4), (25, 7), (36, 9), (115, 7), (322, 7), (1007, 8))
        for case in cases:
            self.assertEqual(add_digits.sum_number_digits(case[0]), case[1])

        # Test numbers with multiple passes
        cases = ((89, 8), (57, 3), (165, 3), (354, 3), (769, 4), (954, 9))
        for case in cases:
            self.assertEqual(add_digits.sum_number_digits(case[0]), case[1])


if __name__ == "__main__":
    unittest.main()
