def balance_list(list_1, list_2):

    length_1 = len(list_1)
    length_2 = len(list_2)

    if length_1 - length_2 >= 2:
        while len(list_1) - len(list_2) >= 2:
            list_2.append(list_1.pop())
        return list_1, list_2

    elif length_2 - length_1 > 2:
        while len(list_2) - len(list_1) >= 2:
            list_1.append(list_2.pop())
        return list_1, list_2

    else:
        return list_1, list_2