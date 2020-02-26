import unittest
import rearrange

class TestRearrange(unittest.TestCase):

    def test_rearrange(self):
        # Test one digit numbers
        for i in range(10):
            self.assertEqual(rearrange.rearrange(i), 0)


if __name__ == '__main__':
    unittest.main()
