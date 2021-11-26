# Given an n x n array, return the array elements arranged from outermost elements to the middle element,
# traveling clockwise.
#
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:
#
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]

# NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array
# in a clockwise snail shell pattern.
#
# NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].

# pseudocode
# 1. make a copy of array of arrays
#   traverse the array of arrays with modification/deletion
#   if empty array, return it
#   while array:
# 2. for loop traverse the first set of array form left to right
#   3. delete the first array set in the matrix
# 4. then traverse down till the last element of the last array set
#   5. delete the last element of each array set traversed
# 6. traverse backward to the first element of the last array set
#   7. delete all elements in the last array set
# 8. traverse upward from the first element in the last array set to the first array set
# 9. delete all the first elements traversed
# 10. repeat step 1
import collections


def snail_sort(snail_map):
    result = []
    copy_snail_map = snail_map.copy()
    temp_snail_map = collections.deque(copy_snail_map)
    print('copy of snail map before iteration: ', temp_snail_map)
    for arrays in temp_snail_map:
        array = collections.deque(arrays)
        print('array sets in arrays: ', array)
        if array:
            x = array.popleft()
            print('this should be the single digit in an array set popped from left: ', x)
            result.append(x)
            # for i in range(0, len(arrays)):
            #     str_i = str(arrays[i])
            #     x = arrays[i].popleft()
            #     print('this should be the single digit in an array set: ', x)
            #     result.append(int(x))
        if not array:
            temp_snail_map.remove(array)
    print('should be empty: ', temp_snail_map)
    return result


snail_map = [[1, 2, 3],
             [8, 9, 4],
             [7, 6, 5]]

print('result of snail map 1: ', snail_sort(snail_map))


def demo_spiral_traversal(matrix):
    res = []
    if len(matrix) == 0:
        return res
    row_begin = 0
    row_end = len(matrix) - 1
    col_begin = 0
    col_end = len(matrix[0]) - 1

    while row_begin <= row_end and col_begin <= col_end:
        for i in range(col_begin, col_end + 1):
            res.append(matrix[row_begin][i])
        row_begin += 1

        for i in range(row_begin, row_end + 1):
            res.append(matrix[i][col_end])
        col_end -= 1

        if row_begin <= row_end:
            for i in range(col_end, col_begin - 1, -1):
                res.append(matrix[row_end][i])
        row_end -= 1

        if col_begin <= col_end:
            for i in range(row_end, row_begin - 1, -1):
                res.append(matrix[i][col_begin])
        col_begin += 1

    return res


def snail_sort_with_delete(array):
    results = []
    while len(array) > 0:
        # go right
        results += array[0]
        del array[0]

        if len(array) > 0:
            # go down
            for i in array:
                results += [i[-1]]
                del i[-1]

            # go left
            if array[-1]:
                results += array[-1][::-1]
                del array[-1]

            # go top
            for i in reversed(array):
                results += [i[0]]
                del i[0]

    return results


if __name__ == "__main__":
    matrix_2 = [[1, 2, 3, 4],
                [8, 9, 4, 5],
                [3, 2, 7, 1],
                [7, 6, 5, 3]]
    matrix = [[1, 2, 3],
              [8, 9, 4],
              [7, 6, 5]]
    print('demo_spiral_traversal result: ', demo_spiral_traversal(matrix))
    print('snail_sort_with_delete result: ', snail_sort_with_delete(matrix_2))
    print('snail_sort result: ', snail_sort(matrix))
