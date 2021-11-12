from challenge import max_subarray_sum


def test_max_subarray_sum():
    test_array1 = max_subarray_sum.max_subarray_sum_finder([1, 2, 3])
    test_array2 = max_subarray_sum.max_subarray_sum_finder([])
    test_array3 = max_subarray_sum.max_subarray_sum_finder([1, -1, 0, 1, 2])
    assert test_array1 == 6
    assert test_array2 == 0
    assert test_array3 == 3
