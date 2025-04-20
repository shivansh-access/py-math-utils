import unittest
from unittest.mock import patch

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


from numbers.number_checker import (
    if_number_is_odd_or_even
)

class TestNumberCheckerFunctions(unittest.TestCase):
    def test_if_number_is_odd_or_even(self):
        # Test with an even number
        result = if_number_is_odd_or_even(4)
        self.assertEqual(result, "4 is even")

        # Test with an odd number
        result = if_number_is_odd_or_even(5)
        self.assertEqual(result, "Odd")

        # Test with zero
        result = if_number_is_odd_or_even(0)
        self.assertEqual(result, "Even")