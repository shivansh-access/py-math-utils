def area_of_a_square(len):
    print(f"The area of given square of length {len}: {len * len}")
    return f"The area of given square of length {len}: {len * len}"


def perimeter_of_a_square(len):
    print(f"The perimeter of given square of length {len}: {len * 4}")
    return f"The perimeter of given square of length {len}: {len * 4}"


def area_of_a_rectangle(len, breadth):
    print(f"The area of given the rectange of length {len} and breadth {breadth}: {len * breadth}")
    return f"The area of given the rectange of length {len} and breadth {breadth}: {len * breadth}"


def perimeter_of_a_rectangle(len, breadth):
     print(f"The perimeter of the given rectangle of length {len} and breadth {breadth}: {(len + breadth) * 2}")
     return f"The perimeter of the given rectangle of length {len} and breadth {breadth}: {(len + breadth) * 2}"


def area_of_a_circle(radius):
    print(f"The area of given circle of radius {radius}: {round(3.14 * radius * radius, 2)}")
    return f"The area of given circle of radius {radius}: {round(3.14 * radius * radius, 2)}"


def circumference_of_circle(radius):
    print(f"The circumference of the given circle of radius {radius}: {round(2 * 3.14 * radius, 2)}")
    return f"The circumference of the given circle of radius {radius}: {round(2 * 3.14 * radius, 2)}"


def area_of_a_triangle(base, height):
    print(f"The area of given triangle of base {base} and height {height}: {round(0.5 * base * height, 2)}")
    return f"The area of given triangle of base {base} and height {height}: {round(0.5 * base * height, 2)}"


def perimeter_of_a_triangle(side1, side2, side3):
    print(f"The perimeter of the given triangle of side1 {side1}, side2 {side2} and side3 {side3}: {side1 + side2 + side3}")
    return f"The perimeter of the given triangle of side1 {side1}, side2 {side2} and side3 {side3}: {side1 + side2 + side3}"
 
