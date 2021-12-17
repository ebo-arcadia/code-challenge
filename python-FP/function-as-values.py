# use functions as values which can be passed to other functions

def plus_one(x):
    return x + 1


# repeat twice as a higher order function takes a function func as an argument
def repeat_twice(func):
    # use input function func to construct a new function plus 2
    def plus_two(x):
        return func(func(x))
    return plus_two


plus_2 = repeat_twice(plus_one)
print(plus_2(0))
print(plus_2(1))
print(plus_2(2))


# another example
def outer_func(name):
    return "value of name param is: " + name

def func_construct_with_another_func(f):
    return f + "string cat by func construct with another func"

def higher_order_function_constructor(func_construct_with_another_func):
    def inner_func(name):
        return func_construct_with_another_func(name)
    return inner_func

new_func = higher_order_function_constructor(outer_func)
print(new_func("John"))

# yet another simpler example
def func_1(x):
    return x + 2

def repeat_func(func):
    def func_constructor(x):
        return func(func(1))
    return func_constructor

func_2 = repeat_func(func_1)
print(func_2(1))
print(func_1(func_1(1)))
