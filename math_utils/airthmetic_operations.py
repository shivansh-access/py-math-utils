def sum_of_two_numbers(num1, num2):
    print(f"Returning the sum of of numbers {num1} and {num2}")
    return num1 + num2


def print_comma_seperated_numbers(num1, num2, num3):
    print(f"num1, num2, num3")
    

def finding_the_biggest_number_of_two(num1, num2):
    if num1 >= num2:
     return num1
    else:
      return num2    
    

def finding_the_biggest_number_of_three(num1, num2, num3):
   if num1 >= num2:
       if num1 >= num3:
           return num1
       else:
           return num3
   elif num2 >= num3:
       return num2
   else:
       return num3     

