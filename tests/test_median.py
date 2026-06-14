from my_app.median import find_median

def test_find_median():

    #Arrange
    expected_1 = 2
    expected_2 = 5
    expected_3 = None

    test_numbers_1 = [1, 2, 1000]
    test_numbers_2 = [1, 2, 3, 4]
    test_numbers_3 = []

    #Act
    actual_1 = find_median(test_numbers_1)
    actual_2 = find_median(test_numbers_2)
    actual_3 = find_median(test_numbers_3)

    #Assert
    assert actual_1 == expected_1
    assert actual_2 == expected_2
    assert actual_3 == expected_3