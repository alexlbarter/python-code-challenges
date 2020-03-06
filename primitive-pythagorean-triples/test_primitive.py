import unittest
import primitive


class MyTestCase(unittest.TestCase):
    def test_primitive(self):
        cases = (([4, 5, 3], True), ([7, 12, 13], False), ([39, 15, 36], False), ([77, 36, 85], True))
        for case in cases:
            self.assertEqual(primitive.is_primitive(case[0]), case[1])


if __name__ == '__main__':
    unittest.main()
