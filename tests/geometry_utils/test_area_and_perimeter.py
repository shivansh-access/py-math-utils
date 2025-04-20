import unittest
from unittest.mock import patch

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


from geometry_utils.area_and_perimeter import (
    area_of_a_square,
    perimeter_of_a_square,
    area_of_a_rectangle,
    perimeter_of_a_rectangle,
    area_of_a_circle,
    circumference_of_circle,
    area_of_a_triangle,
    perimeter_of_a_triangle
)


class TestAreaAndPerimeterFunctions(unittest.TestCase):

    def test_area_of_a_square(self):
        # Test with a square of length 4
        expected1 = "The area of given square of length 4: 16"
        result1 = area_of_a_square(4)
        self.assertEqual(result1, expected1)

        expected2 = "The area of given square of length 5: 25"
        result2 = area_of_a_square(5)
        self.assertEqual(result2, expected2)


    def test_perimetre_of_a_square(self):
        # test with a square of lenght of 6
        expected= "The perimeter of given square of length 6: 24"
        result = perimeter_of_a_square(6)
        self.assertEqual(result, expected)

    def test_area_of_a_rectangle(self):
        # test with a rectangle of length 4 and breadth 5
        expected = "The area of given the rectange of length 4 and breadth 5: 20"
        result = area_of_a_rectangle(4, 5)
        self.assertEqual(result, expected)


    def test_perimeter_of_a_rectangle(self):
        # test with a rectangle of length 6 and breadth 5
        expected = "The perimeter of the given rectangle of length 6 and breadth 5: 22"
        result = perimeter_of_a_rectangle(6, 5)
        self.assertEqual(result, expected) 


    def test_area_of_a_circle(self):
        # test with a circle of radius 3
        expected = "The area of given circle of radius 3: 28.26"
        result = area_of_a_circle(3)
        self.assertEqual(result, expected)


    def test_circumference_of_circle(self):
        # test with a circle of radius 3
        expected = "The circumference of the given circle of radius 7: 43.96"
        result = circumference_of_circle(7)
        self.assertEqual(result, expected)


    def test_area_of_a_triangle(self):
        # test with a triangle of base 7 and height 5
        expected = "The area of given triangle of base 7 and height 5: 17.5"
        result = area_of_a_triangle(7, 5)
        self.assertEqual(result, expected)


    def test_perimeter_of_a_triangle(self):
        # test with a triangle of sides 8, 5, and 5
        expected = "The perimeter of the given triangle of side1 8, side2 5 and side3 5: 18"
        result = perimeter_of_a_triangle(8, 5, 5)
        self.assertEqual(result, expected)     


if __name__ == '__main__':
    unittest.main()

