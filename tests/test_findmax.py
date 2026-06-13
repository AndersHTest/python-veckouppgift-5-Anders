from my_app.find_max_value import *

def test_find_max():

    #Arrange
    expected_1 = 34
    expected_2 = None

    test_find_1 = [1, 12, 34, 22, 2]
    test_find_2 = []

    #Act
    actual_1 = find_max(test_find_1)
    actual_2 = find_max(test_find_2)

    #Assert
    assert actual_1 == expected_1
    assert actual_2 == expected_2


def test_find_second_largest():

    #Arrange
    expected_1 = 22
    expected_2 = None

    test_find_1 = [1, 12, 34, 22, 2]
    test_find_2 = []

    #Act
    actual_1 = find_2nd_max(test_find_1)
    actual_2 = find_2nd_max(test_find_2)

    #Assert
    assert actual_1 == expected_1
    assert actual_2 == expected_2
