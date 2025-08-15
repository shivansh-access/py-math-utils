def sumcalculator(num1, num2):
    print(f"the sum of these two numbers {num1}, {num2}")
    print("the sum of these two numbers " + str(num1) + ", " + str(num2))
    return num1 + num2

def init (num1, num2):
    print("the sum of these two numbers " + num1 + ", " + num2)

# print(sumcalculator(5, 7))
# init("51", "71")




def determineTypeOfTriangle(a, b, c):
    if((a<=0 or b<=0 or c<=0) or
       ((a + b + c) != 180)):
        print("Not a triangle")
    elif(a==90 or b==90 or c==90):
        print("Right angled triange")
    elif(a < 90 and b < 90 and c < 90):
        print("Acute angled traingle")
    else:
        print("Obtuse angled traingle")
    

      
determineTypeOfTriangle(90, 90, 10)
determineTypeOfTriangle(60, 60, 60)
determineTypeOfTriangle(100, 60, 20)
determineTypeOfTriangle(90, 35, 55)



def Intro(name, age):
    print(f"Hello my name is {name} my age is {age}.")
    return {name} ,{age}

# Intro("Shivansh", 10)