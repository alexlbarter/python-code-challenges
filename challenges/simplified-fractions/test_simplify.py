import unittest
import simplify


class TestSimplify(unittest.TestCase):

    def test_simplify(self):
        # Basic tests
        cases = (("4/6", "2/3"), ("10/11", "10/11"), ("100/400", "1/4"), ("8/4", "2"))
        for case in cases:
            self.assertEqual(simplify.simplify(case[0]), case[1])

    def test_invalid_input(self):
        # Test invalid input
        with self.assertRaises(ValueError):
            cases = (5, "5", "abc", "ab/c")
            for case in cases:
                simplify.simplify(case)

