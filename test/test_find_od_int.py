from challenge import find_od_int


def test_func():
    result = find_od_int.find_od_int([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5])
    assert result == 5
