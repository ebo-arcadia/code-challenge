from challenge import find_od_int


def test_func():
    result1 = find_od_int.find_od_int([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5])
    result2 = find_od_int.find_od_int([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5])
    result3 = find_od_int.find_od_int([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5])
    result4 = find_od_int.find_od_int([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1])
    result5 = find_od_int.find_od_int([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10])
    assert result1 == 5
    assert result2 == -1
    assert result3 == 5
    assert result4 == 10
    assert result5 == 1
