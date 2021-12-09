# a lambda function is a small anoymous function
# it cab take any number of arguments, but can only have one expression
# why use it? the benefit comes when it is used inside another function

# example
# first define a function
def double_num(double_factor):
    return lambda n: n * double_factor


# construct a function with the defined function
double_2_times = double_num(2)
double_3_times = double_num(3)
print(double_2_times(10))
print(double_3_times(10))

# another example
sum_two = lambda x, y: x + y
sum_two_and_another = lambda x, y, z: sum_two(z, sum_two(x, y))

print(sum_two_and_another(2, 3, 9))
