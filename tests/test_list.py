from my_app.list import *


def test_empty_list():
    expected = [] # ???

    actual = empty_list([]) # ???

    assert actual == expected


def test_number_list():
    # TODO: testa med listor som har ett, två respektive fem element.

    x = [5]
    y = [1, 3]
    z = [1, 2, 3, 4, 5]

    assert sum_list(x) == 5
    assert sum_list(y) == 4# ???
    assert sum_list(z) == 15 # ???
