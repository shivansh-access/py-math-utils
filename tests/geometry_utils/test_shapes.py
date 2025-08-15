import unittest
from unittest.mock import patch

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


from geometry_utils.shapes import (
    determine_type_of_triangle
)


class TestShapesFunctions(unittest.TestCase):
    def test_determine_type_of_triangle(self):
        expected1 = "Obtuse"
        result1 = determine_type_of_triangle(120, 30, 30)
        self.assertEqual(result1, expected1)

        expected2 = "Right-angled"
        result2 = determine_type_of_triangle(90, 45, 45)
        self.assertEqual(result2, expected2)

        expected3 = "Acute"
        result2 = determine_type_of_triangle(60, 60, 60)
        self.assertEqual(result2, expected3)

        expected4 = "Invalid"
        result4 = determine_type_of_triangle(0, 90, 90)
        self.assertEqual(result4, expected4) 

        expected5  = "Invalid"
        result5 = determine_type_of_triangle(180, 0, 0)



if __name__ == '__main__':
    unittest.main()