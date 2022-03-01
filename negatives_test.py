from unittest import result

from negatives import lista

def test_negative_test_van_benne():
    #Given
    #When
    result = lista([1,-5,1,13,-7,9,11,21,-33,44,55,11,22,30,11])
    #Then
    assert result == 3

def test_negative_test_nincs_benne():
    #Given
    #When
    result = lista([1,5,1,13,7,9,11,21,33,44,55,11,22,30,11])
    #Then
    assert result == 1

def test_negative_test_ures_lista():
    #Given
    #When
    result = lista([])
    #Then
    assert result == 2






