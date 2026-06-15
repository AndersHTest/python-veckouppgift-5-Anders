from my_app.balance_list import balance_list

def test_balance_list():

    #Arrange

    test_list_1 = [20, "Träd", "Fisk", 30, 50]
    test_list_2 = ["Häst", 5, 3]

    test_list_3 = [1, 2]
    test_list_4 = [3, 4]

    test_list_5 = [1, 2, 3, 4, 5]
    test_list_6 = [1, 2, 3, 4]

    test_list_7 = [1, 2, 3, 4]
    test_list_8 = [1, 2, 3, 4, 5]

    test_list_9 = [1, 2, 3]
    test_list_10 = [1, 2, 3, 4, 5]

    expected_1 = ([20, "Träd", "Fisk", 30], ["Häst", 5, 3, 50])
    expected_2 = ([1, 2], [3, 4])
    expected_3 = ([1, 2, 3, 4, 5], [1, 2, 3, 4])
    expected_4 = ([1, 2, 3, 4], [1, 2, 3, 4, 5])
    expected_5 = ([1, 2, 3, 5], [1, 2, 3, 4])


    #Act

    actual_1 = balance_list(test_list_1, test_list_2)
    actual_2 = balance_list(test_list_3, test_list_4)
    actual_3 = balance_list(test_list_5, test_list_6)
    actual_4 = balance_list(test_list_7, test_list_8)
    actual_5 = balance_list(test_list_9, test_list_10)


    #Assert

    assert actual_1 == expected_1
    assert actual_2 == expected_2
    assert actual_3 == expected_3
    assert actual_4 == expected_4
    assert actual_5 == expected_5