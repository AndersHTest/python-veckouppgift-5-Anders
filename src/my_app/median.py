def find_median(numbers):

    count_element = len(numbers)
    sorted_list = sorted(numbers)
    sum_list = sum(numbers)

    if not numbers:
        return None

    elif count_element % 2 == 0:
        return sum_list / 2

    else:
        return sorted_list[count_element // 2]
