def generate_table(number, limit):
    table = []
    for i in range(1, limit + 1):
        table.append(f"{number} x {i} = {number * i}")
    return table


def print_table(number, limit):
    print("-- Welcome to the multiplication table generator --")
    print(f"Printing table of {number} upto {limit}:")
    table = generate_table(number, limit)
    for line in table:
        print(line)

