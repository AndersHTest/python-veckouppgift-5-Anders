from my_app.count_words import count_words

def test_count_words():

    #Arrange
    expected_1 = 5
    expected_2 = 6

    test_sentence_1 = "Detta är en serie tecken"
    test_sentence_2 = "D3.*a /r också en seri3 t3c-3n."

    #Act
    actual_1 = count_words(test_sentence_1)
    actual_2 = count_words(test_sentence_2)

    #Assert
    assert actual_1 == expected_1
    assert actual_2 == expected_2