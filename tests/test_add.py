from my_app.list import add

def test_add():
    #Arrange
    expected = 3
    x = 1
    y = 2

    #Act
    actual = add(x, y)

    #Assert
    assert actual == expected