import unittest
from triangle import *


class circleTestCase(unittest.TestCase):
    def test_right_area(self):
        res = area(5,3)
        self.assertEqual(res, 7.5)

    def test_str_argument_area(self):
        res = area("5","3")
        self.assertEqual(res, 7.5)

    def test_zero_area(self):
        res = area(0,5)
        self.assertEqual(res, 0)

    def test_right_perimeter(self):
        res = perimeter(3,2,2)
        self.assertEqual(res, 7)

    def test_str_argument_perimeter(self):
        res = perimeter("3","2","2")
        self.assertEqual(res, 7)

    def test_zero_perimeter(self):
        res = perimeter(0,0,2)
        self.assertEqual(res, 2)


