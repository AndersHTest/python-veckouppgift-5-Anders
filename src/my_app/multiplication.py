def multiplication_table(n, limit):

    table = []
    counter = 1

    if n == 0:
        return [0]

    elif limit <= 0:
        info = "The limit has to be a positive integer."
        return info

    else:
        for i in range(limit):
            x = n * counter
            table.append(x)
            counter += 1

    return table
