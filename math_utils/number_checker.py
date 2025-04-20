def if_number_is_odd_or_even(number):
    remainder = number % 2
    if remainder == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"

