def find_max(lista):
    if len(lista) == 0:
        return None
    elif len(lista) > 0:
        highest_value = max(lista)
        return highest_value
    else:
        return None


def find_2nd_max(lista):
    if len(lista) == 0:
        return None

    elif len(lista) > 0:
        lista.remove(max(lista))
        second_largest_value = max(lista)
        return second_largest_value

    else:
        return None