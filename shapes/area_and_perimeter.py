def area_and_perimter_of_square(len):
    print(f"The area of given square of length {len}: {len * len}")
    print(f"The perimeter of given square of length {len} : {len * 4}")


def area_and_perimter_of_rectangle(len, breadth):
    print(f"The area of given rectange of length {len} and breadth {breadth}: {len * breadth}")
    print(f"The primetre of the given rectangle of length {len} and breadth {breadth}: {(len + breadth) * 2}") 


def area_and_circumference_of_circle(radius):
    print(f"The area of given circle of radius {radius}: {round(3.14 * radius * radius, 2 )}")
    print(f"The circumference of the given circle of radius {radius}: {round(2 * 3.14 * radius, 2)}")

def area_and_perimeter_of_triangle(base, height, side1, side2):
    print(f"The area of given triangle of base {base} and height {height}: {round(0.5 * base * height, 2)}")
    print(f"The perimeter of the given triangle of base {base}, side1 {side1} and side2 {side2}: {base + side1 + side2}")

 