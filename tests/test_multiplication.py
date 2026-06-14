from my_app.multiplication import multiplication_table

def test_find_median():

    #Arrange
    expected_1 = [3, 6, 9, 12]
    expected_2 = [0]
    expected_3 = "The limit has to be a positive integer."
    expected_4 = [-3, -6, -9, -12, -15]

    test_number_1 = 3
    test_limit_1 = 4

    test_number_2 = 0
    test_limit_2 = 5

    test_number_3 = 5
    test_limit_3 = 0

    test_number_4 = -3
    test_limit_4 = 5

    #Act
    actual_1 = multiplication_table(test_number_1, test_limit_1)
    actual_2 = multiplication_table(test_number_2, test_limit_2)
    actual_3 = multiplication_table(test_number_3, test_limit_3)
    actual_4 = multiplication_table(test_number_4, test_limit_4)

    #Assert
    assert actual_1 == expected_1
    assert actual_2 == expected_2
    assert actual_3 == expected_3
    assert actual_4 == expected_4