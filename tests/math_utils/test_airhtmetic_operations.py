import unittest
from unittest.mock import patch

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


from math_utils.airthmetic_operations import (
    sum_of_two_numbers, 
    finding_the_biggest_number_of_two,
    finding_the_biggest_number_of_three,
    finding_the_biggest_number,
    find_sum_of_numbers_in_an_array
)


class TestAirthmeticOperations(unittest.TestCase):
    
    def test_sum_of_two_numbers(self):
        result = sum_of_two_numbers(40, 60) 
        self.assertEqual(result, 100)


    def  test_finding_the_biggest_number_of_two(self):
         result1 = finding_the_biggest_number_of_two(60, 80)
         self.assertEqual(result1, 80)

         result2 = finding_the_biggest_number_of_two(100, 80)
         self.assertEqual(result2, 100)

         result3 = finding_the_biggest_number_of_two(120, 120)
         self.assertEqual(result3, 120)

   
    def test_finding_the_biggest_number_of_three(self):
        result1 = finding_the_biggest_number_of_three(50, 70, 99)
        self.assertEqual(result1, 99)

        result2 = finding_the_biggest_number_of_three(50, 100, 99)
        self.assertEqual(result2, 100)

        result3 = finding_the_biggest_number_of_three(110, 70, 99)
        self.assertEqual(result3, 110)

        result4 = finding_the_biggest_number_of_three(-100, 70, 199)
        self.assertEqual(result4, 199)

        result5 = finding_the_biggest_number_of_three(50, 50, 50)
        self.assertEqual(result5, 50)


    def test_finding_the_biggest_number(self):
        result1 = finding_the_biggest_number([100, 110, 1110, 10, 20, 50, 75, 43, 89])
        self.assertEqual(result1, 1110)

        result1 = finding_the_biggest_number([-100, 100, 0, 150])
        self.assertEqual(result1, 150)

    def test_find_sum_of_numbers_in_an_array(self):
        result1 = find_sum_of_numbers_in_an_array([100, 100, 500])
        self.assertEqual(result1, 700)


        result2 = find_sum_of_numbers_in_an_array([100, -50, 100,-25])
        self.assertEqual(result2, 125)

                                                      

if __name__ == '__main__':
    unittest.main()

