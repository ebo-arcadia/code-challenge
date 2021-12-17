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
multiply_two_and_three = multiply_two_nums(2)
multiple_ten_again = multiply_two_and_three(10)
print(multiple_ten_again)

print("-----------------------")

# partial application
# partially applying a function means to pre-fill the argument with the original function
# see another file in this directory for more detail

# currying

