from my_app.Temperatur import c_to_f

def test_temp():
    #Arrange
    expected_1 = 14
    expected_2 = 104
    expected_3 = None

    test_f_1 = -10
    test_f_2 = 40
    test_f_3 = -275

    #Act
    actual_1 = c_to_f(test_f_1)
    actual_2 = c_to_f(test_f_2)
    actual_3 = c_to_f(test_f_3)

    #Assert
    assert actual_1 == expected_1
    assert actual_2 == expected_2
    assert actual_3 == expected_3
