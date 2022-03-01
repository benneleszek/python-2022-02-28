from sum import sumlista


def test_sum_normal():
    #Given
    #When
    result = sumlista([1,2,3,4])
    #Then
    assert result == 10

def test_sum_negativ():
    #Given
    #When
    result = sumlista([1,-2,-3,-4])
    #Then
    assert result == -8

def test_sum_ures():
    #Given
    #When
    result = sumlista([])
    #Then
    assert result == 0