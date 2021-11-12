# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or
# list of integers:
#
# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) # should be 6: [4, -1, 2, 1] Easy case is when the list is made up of
# only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative
# numbers, return 0 instead.
#
# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid
# sublist/subarray.

# pseudocode
# iterate array
# if all numbers are positive, add them up and store the total in a variable then return the variable
# if empty array, return 0
# else: numbers are both positive and negative
# add all numbers first iteration
# add all numbers except the first num the second iteration
# compare the two and keep the larger one
# add all numbers except the first and second numbers the third iteration
# compare the larger sum from previous comparison to the new total and keep the larger one
# finish iteration
# keep the largest total and return it


def max_subarray_sum_finder(array):
    current_max = 0
    max_till_now = 0
    for i in range(0, len(array)):
        current_max = max(array[i], current_max + array[i])
        max_till_now = max(current_max, max_till_now)
        # max_ending_here = max_ending_here + array[i]
        # if len(array) != 0 and array[i] > 0:
        #     total += array[i]
        # elif len(array) == 0 or array[i] < 0:
        #     return total
        # if max_ending_here < 0:
        #     max_ending_here = 0
        # elif max_till_now < max_ending_here:
        #     max_till_now = max_ending_here
    return max_till_now


test_array1 = [1, 2, 3]
test_array2 = []
test_array3 = [1, -1, 0, 1, 2]

print('all numbers in array are positive: ', max_subarray_sum_finder(test_array1))
print('empty array: ', max_subarray_sum_finder(test_array2))
print('fixed positive and negative numbers: ', max_subarray_sum_finder(test_array3))