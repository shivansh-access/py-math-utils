def generate_table(num , limit):
    if limit <= 0:
        raise ValueError("Limit must be a positive integer.")

    table = []
    for x in range (1, limit + 1):
        table.append(f"{num} * {x} = {num * x}")

    return table


def print_table(num, limit):
    table = generate_table(num, limit)
    for line in table:
        print(line)