# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.

# pseudocode
# 1. define what is odd
# 2. iterate all int in the array
# 3. count num of occurrence of each int
#       if num meet odd definition
#           return the ini

def find_od_int(arr_of_int):
    for i in arr_of_int:
        if arr_of_int.count(i) % 2 != 0:
            return i



