def find_median(numbers):

    count_element = len(numbers)
    sorted_list = sorted(numbers)

    if not numbers:
        return None

    elif count_element % 2 == 0:
        if count_element > 2:
            mitten = count_element // 2
            mitten_1 = sorted_list[mitten - 1]
            mitten_2 = sorted_list[mitten]
            mitten_tot = mitten_1 + mitten_2
            medel = mitten_tot / 2
            return medel

        else:
            meddelande = "Listan var för kort."
            return meddelande

    else:
        return sorted_list[count_element // 2]
