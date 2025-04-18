import unittest
from unittest.mock import patch

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from shapes.area_and_perimeter import (
    area_and_perimter_of_square, 
    area_and_perimter_of_rectangle, 
    area_and_circumference_of_circle, 
    area_and_perimeter_of_triangle
)

class TestAreaAndPerimeterFunctions(unittest.TestCase):

    @patch('shapes.area_and_perimeter.print') 
    def test_area_and_perimeter_of_square(self, mock_print):
        # Test with a square of length 4
        area_and_perimter_of_square(4)
        mock_print.assert_any_call("The area of given square of length 4: 16")
        mock_print.assert_any_call("The perimeter of given square of length 4: 16")


if __name__ == '__main__':
    unittest.main()