from unittest import result

from number_compare import nagyobb15


def test_larger_with_big_number():
    #Given
    #When
    result = nagyobb15(100)
    #Then
    assert result == True


def test_larger_with_big_number_short():
    assert nagyobb15(100)


def test_larger_with_big_number_smaller():
    assert not nagyobb15(10)


def test_larger_with_big_number_equal():
    assert not nagyobb15(15)


def test_larger_with_big_number_negative():
    assert not nagyobb15(-2)