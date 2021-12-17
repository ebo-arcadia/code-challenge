# what is 2-D array?
# it is an array within an array or an array of arrays
# in which each element of an array is also an array
# the position of an data element is referred by two indices instead of one
# think of a table with rows and columns

# how to represent a table below as a 2-D array?
# Day 1 - 11 12 5 2
# Day 2 - 15 6 10
# Day 3 - 10 8 12 5
# Day 4 - 12 15 8 6

# create a 2-D array
two_d_array_days = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]
print(two_d_array_days)
print("--------------------")

# how to access data elements in a 2-D array?
first_child_arr_ele_in_parent_arr = two_d_array_days[0]
first_elem_in_first_child_a = two_d_array_days[0][0]
print("first_child_arr_ele_in_parent_arr: ", first_child_arr_ele_in_parent_arr)
print("first_elem_in_first_child_a: ", first_elem_in_first_child_a)
print("--------------------")

# how to print out the entire parent array with all the elements in it?
for child_arrays in two_d_array_days:
    for el in child_arrays:
        print(el, end=" ")
print("--------------------")

# how to insert values in a 2-D array?
# make a copy of the original 2-d array
new_two_d_array = two_d_array_days.copy()
print("copy and create a new 2-D array: ", new_two_d_array)
new_two_d_array.insert(len(new_two_d_array), [-1, -2, -10, -999])
print("updated new 2-D array inserting a new array at the end: ", new_two_d_array)
print("--------------------")

# how to update values in a 2-D array?
string_2_d_array = [['row1', 'row2', 'row3'], ['col1', 'col2', 'col3'], ['val1', 'val2', 'val3']]
print("original string 2-D array: ", string_2_d_array)
string_2_d_array[0] = ['updated_row1', 'updated_row2', 'updated_row3'] # update the first child array
string_2_d_array[2][2] = 'location' # update the 3rd element in the last child array
print("updated string 2-D array: ", string_2_d_array)
print("--------------------")

# how to delete values from a 2-D array?
# what can one delete?

# how to remove the entire 3rd child array?

copy_string_2_d_array = string_2_d_array.copy()
print("original string 2-D array: ", copy_string_2_d_array)
del copy_string_2_d_array[2]
del(copy_string_2_d_array[1][1])
print("updated string 2-D array with deletion: ", copy_string_2_d_array)




