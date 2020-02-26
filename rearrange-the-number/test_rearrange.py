import unittest
import rearrange


class TestRearrange(unittest.TestCase):

    def test_rearrange(self):
        # Test 1 digit numbers
        for i in range(10):
            self.assertEqual(rearrange.rearrange(i), 0)

        # Test larger numbers
        cases = ((972882, 760833), (3320707, 7709823), (90010, 90981))
        for case in cases:
            self.assertEqual(rearrange.rearrange(case[0]), case[1])


if __name__ == '__main__':
    unittest.main()
