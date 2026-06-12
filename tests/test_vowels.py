from my_app.vowels import count_vowels

def test_no_vowels():
    #Arrange
    expected_1 = 0
    expected_2 = 0
    expected_3 = 0
    expected_4 = 0
    expected_5 = 8
    expected_6 = 9
    expected_7 = 5

    test_input_1 = "qwrt"
    test_input_2 = "Tt"
    test_input_3 = "123 123"
    test_input_4 = ""
    test_input_5 = "aOåÄöiöö"
    test_input_6 = "aeiouyåäö"
    test_input_7 = "Du är en stjärna"

    #Act
    actual_1 = count_vowels(test_input_1)
    actual_2 = count_vowels(test_input_2)
    actual_3 = count_vowels(test_input_3)
    actual_4 = count_vowels(test_input_4)
    actual_5 = count_vowels(test_input_5)
    actual_6 = count_vowels(test_input_6)
    actual_7 = count_vowels(test_input_7)

    #Assert
    assert count_vowels(test_input_1) == 0
    assert count_vowels(test_input_2) == 0
    assert count_vowels(test_input_3) == 0
    assert count_vowels(test_input_4) == 0
    assert count_vowels(test_input_5) == 8
    assert count_vowels(test_input_6) == 9
    assert count_vowels(test_input_7) == 5