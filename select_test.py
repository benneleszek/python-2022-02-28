from numberselect import numbersl


def test_select_normal():
    #Given
    #When
    result = numbersl([1,2,3])
    #Then
    assert result == [-1,-2,-3]