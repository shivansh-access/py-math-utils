def generate_table(number, limit):
    table = []
    for i in range(1, limit + 1):
        table.append(f"{number} x {i} = {number * i}")
    return table


def print_table(number, limit):
    table = generate_table(number, limit)
    for line in table:
        print(line)


# Example usage:
if __name__ == "__main__":
    num = 5
    lim = 10
    print_table(num, lim)