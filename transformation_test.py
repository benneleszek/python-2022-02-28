from transformation import transf


def test_select_normal():
    #Given
    #When
    result = transf([1,2,3])
    #Then
    assert result == [2,4,6]

def test_select_nulla():
    #Given
    #When
    result = transf([0])
    #Then
    assert result == [0]

def test_select_negativ():
    #Given
    #When
    result = transf([-1,-2])
    #Then
    assert result == [-2,-4]