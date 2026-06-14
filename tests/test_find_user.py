from my_app.find_user import *

def test_find_user():

    #Arrange
    expected_1 = ['Anna', 'Anders', 'Anton']
    expected_2 = ['Lisa', 'Linus']
    expected_3 = ['Victor', 'Viktoria']

    test_user_input_1 = 'An'
    test_user_input_2 = 'Li'
    test_user_input_3 = 'Vi'

    test_master_list = ['Anna', 'Anders', 'Lisa', 'Per', 'Anton', 'Linus', 'Victor', 'Viktoria']

    #Act
    actual_1 = autocomplete_list(test_user_input_1, test_master_list)
    actual_2 = autocomplete_list(test_user_input_2, test_master_list)
    actual_3 = autocomplete_list(test_user_input_3, test_master_list)

    #Assert
    assert actual_1 == expected_1
    assert actual_2 == expected_2
    assert actual_3 == expected_3