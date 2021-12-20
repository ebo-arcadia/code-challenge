from inspect import signature


# Arity
# The number of arguments a function takes

def arity_two_concat(x: str, y: str) -> str:
    two_strs = ""
    two_strs += x + y
    return two_strs


num_of_args = len(signature(arity_two_concat).parameters)
print("what is the arity of function arity_two_concat?: ", num_of_args)
print("-----------------------")

# higher-order function
# a function that takes a function as an argument

filter_higher_func = lambda predicate, xs: [x for x in xs if predicate(xs)]
is_a_func_as_args = lambda type_right: lambda x: type(x) is type_right

if_int = filter_higher_func(is_a_func_as_args(int), [0, "0", 2, "2", "None", None])
print("filter an iterable and only returns type integer: ", if_int)
print("-----------------------")

# closure scope which captures the local variables of a function for access even after the execution of the function
# thus moved out of the block in which those variable are defined

multiply_two_nums = lambda x: lambda y: x * y
multiply_two = multiply_two_nums(2)
print(multiply_two)
multiple_two_ten = multiply_two(10)
print(multiple_two_ten)

print("-----------------------")

# partial application
# partially applying a function means to pre-fill the argument with the original function
# see another file in this directory for more detail

# currying
# a process of converting a function that takes multiple arguments into a founction that takes those
# arguments one at a time

multiply = lambda x, y: x * y
curried_multiply = lambda x: lambda y: x * y
rt = curried_multiply(11)(3)
print(rt)
three_times_what = curried_multiply(3)
three_times_nine_nine = three_times_what(99)
print(three_times_nine_nine)

print("-----------------------")

# auto-currying
# transforms a function takes multiple arguments into one
# if less that correct numbers of arguments is given
# that function will returns another function to take care of the missing arguments
# the function will evaluate when it gets the correct amount of arguments

from toolz import curry


@curry
def divide_two_num(a, b):
    return a / b


divide_two = divide_two_num(10, 2)  # returns 5
print("given the correct amount of args, function returns: ", divide_two)
one_arg_exec = divide_two_num(100)  # returns (b) = 100 / b
print("given only one args, function returns: ", one_arg_exec)
curried_divide = divide_two_num(100)(50)  # returns 2
print("given two args but in sequence, function returns: ", curried_divide)

print("-----------------------")

# function composition the act of putting two or more functions together to form a new function in such a way that
# the output of one function is passed as an input for another function

def add_two(x):
    return x + 2

def times_ten(y):
    return y * 10

# print the result of composition to first add 2 to a num and then times it with 10
def add_times_comp(n):
    return times_ten(add_two(n))

func_comp = add_times_comp(10)
print("expected result to be 120: ", func_comp)
print("-----------------------")

# Continuation / Continuation Passive Style (CPS)
# concept of a given time in a program, the part of the code that has yet to be executed
# it is often used in asynchronous programming when the program needs to wait to receive data before it continue
# in other words, at any point of time in the program, one can save the state of the execution for later

continue_program_with = lambda data: data

def find_data(n):
    if n <= 2:
        return "done"
    else:
        return continue_program_with


print(find_data(5))

print("-----------------------")

# purity
# see python-FP folder for more detail

# side effects
# see python-FP folder for more details


# idempotent
# it refers to a function does not have side effect with called multiple times with the same input parameters
# therefore, it makes idempotent safer to retry
# the get request API is an example of idempotent operation as it returns the same result with the same request

# func(func(x)) = func(x)
sorted1 = sorted([10, 8, 5, 99, 0])
print("sort a list one time: ", sorted1)
sorted_x_times = sorted(sorted(sorted(sorted(sorted1))))
print("sort a list many time: ", sorted_x_times)

print("-----------------------")

# tacit programming (point-free programming) it is a programming paradigm in which a function definition does not
# include information about its argument but using combinators and function composition
# why it is useful?
# it aims to reduce some argument parameter clutters mapping

map = lambda func: lambda xs: [func(x) for x in xs]
add = lambda a: lambda b: a + b

# not point-free style as 'nums' is an explicit argument
increment_all = lambda nums: map(add(1))(nums)
print("not point free style calling function: ", increment_all)

# points free style as the list is an implicit argument
increment_all_free_style = map(add(2))
print("point free style calling function: ", increment_all_free_style)

print("-----------------------")












