def determine_type_of_triangle(a, b, c):
    if((a <= 0 or b <= 0 or c <= 0) or
       ((a + b + c) != 180)):
        return "Invalid"
    elif(a == 90 or b == 90 or c == 90):
        return "Right-angled"
    elif(a < 90 and b < 90 and c < 90):
        return "Acute"
    else:
        return "Obtuse"

