from my_app.list import *


def test_empty_list():
    #Arrange
    expected = [] # ???
    test_input = []

    #Act
    actual = empty_list(test_input) # ???

    #Assert
    assert actual == expected


def test_number_list():
    # TODO: testa med listor som har ett, två respektive fem element.

    # Arrange
    expected_x = 5
    expected_y = 4
    expected_z = 15

    test_x = [5]
    test_y = [1, 3]
    test_z = [1, 2, 3, 4, 5]

    #Act
    actual_x = sum_list(test_x)
    actual_y = sum_list(test_y)
    actual_z = sum_list(test_z)

    #Assert
    assert actual_x == expected_x
    assert actual_y == expected_y
    assert actual_z == expected_z
