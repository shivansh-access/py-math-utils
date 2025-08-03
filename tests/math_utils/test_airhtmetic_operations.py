import unittest
from unittest.mock import patch

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


from math_utils.airthmetic_operations import sum_of_two_numbers 



class TestAirthmeticOperations(unittest.TestCase):
    
    def test_sum_of_two_numbers(self):
        # test with two numbers
        result = sum_of_two_numbers(40, 60) 
        self.assertEqual(result, 100)


if __name__ == '__main__':
    unittest.main()

