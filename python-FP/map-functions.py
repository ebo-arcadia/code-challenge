# map() function returns object of result after applying a given function to each item of a iterable (list, tuple, etc)
# map(function, iterable)

# example 1

num_tuple = (0, 1, 2, 3, 4, 5)
# apply function to each item in num_tuple
num_times = map(lambda x: x * x, num_tuple)
print("original num_tuple: ", num_tuple)
print("copy of num_tuple with every item doubled: ", list(num_times))

# example 2
num_tuple_x = (11, 22, 33)
num_tuple_y = (101, 202, 303)
combine_num_tuple_x_y = list(map(lambda x, y: x + y, num_tuple_x, num_tuple_y))
print("copy of result adding two num tuples: ", combine_num_tuple_x_y)