from math_utils.table import print_table
from math_utils.airthmetic_operations import sum_of_two_numbers
from geometry_utils.area_and_perimeter import *

if __name__ == "__main__":
    print("-- Welcome to the multiplication table generator! --")
    print_table(7, 10)
    s = sum_of_two_numbers(4, 10)
    print(f"-- Printing sum of two number: 4 and 10 is {s}")

