from operations import add


def test_add():
    #Given
    x = 5
    y = 10
    #When
    result = add (x,y)
    #Then
    assert result == 15


def test_add_simple():
    assert add(5,10) == 15