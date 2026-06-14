from my_app.sort_numbers import is_sorted_ascending

def test_is_sorted_ascending():

    #Arrange
    expected_1 = True
    expected_2 = False

    test_numbers_1 = [1, 2, 3, 4, 5]
    test_numbers_2 = [5, 4, 3, 2, 1]

    #Act
    actual_1 = is_sorted_ascending(test_numbers_1)
    actual_2 = is_sorted_ascending(test_numbers_2)

    #Assert
    assert actual_1 == expected_1
    assert actual_2 == expected_2
