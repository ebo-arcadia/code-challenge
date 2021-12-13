# what is python Itertools?
# what are the benefits of using it?
# a fast, memory-efficient collection of tools for handling/creating iterators
# what are iterators?
# data types that can be used in a for loop

# using itertools
import itertools
import operator

# example tool 1: accumulate()
# problem: given a list of nums, multiple each item, find max, add each num

list_nums = [1, 2, 3, 4, 6, 9]
iter_multiple = itertools.accumulate(list_nums, operator.mul)
iter_sum = itertools.accumulate(list_nums)
iter_max = itertools.accumulate(list_nums, max)

print("testing accumulator(): ")
for i in iter_multiple:
    print(i)
for i in iter_sum:
    print(i)
for i in iter_max:
    print(i)

print("---------------- end")

# example tool 2: combinations()
# example tool 3: count()
# example tool 4: filterfalse()
# example tool 5: groupby()
# example tool 6: permutations


