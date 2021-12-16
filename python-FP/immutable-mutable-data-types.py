# in functional programming, it is recommended to use immutable types instead of mutable
# why? immutable data types ensure functions remain pure with no side effect
# this is important especially for parallel programming when bugs are often introduced by changing the same
# objects in two different processes
# mutable or immutable, is the data still the same after applying the function?

import numpy
from functools import lru_cache
from typing import List

def try_to_change_data_type(x):
    x += x
    return x


a = 10
try_to_change_data_type(a)

b = "a string"
try_to_change_data_type(b)

c = ('a', 'tuple', 'data')
try_to_change_data_type(c)

d = [99, 100, 888]
try_to_change_data_type(d)

e = True
try_to_change_data_type(e)

f = 1.234
try_to_change_data_type(f)

g = ['a', 'list', 'of', 'items']
try_to_change_data_type(g)

h = {'apple': 'a fruit', 'cup': 'a tool'}
# try_to_change_data_type(h) <-- won't work

i = ('a', 'set', 'data')
try_to_change_data_type(i)

j = numpy.array([1, 5, 10])
try_to_change_data_type(j)

# functional programming principle:
# use immutable types for dictionary keys
# in python, what is immutable is also hash-able

dict_immutable = {}

# set tuple as keys in a dictionary
dict_immutable['sun', 'moon'] = 'center', 'side'
print(('sun', 'moon') in dict_immutable)
print('----------------------------')

# convert lists to tuples
# add to the dictionary
my_list = [1, 2, 3]
dict_immutable[tuple(my_list)] = 4
print(dict_immutable)
print('----------------------------')

# convert sets and dictionaries to frozen sets
my_set = ('a', 'b', 'c')
dict_immutable[frozenset(my_set)] = 100
print(dict_immutable)
dict_immutable[frozenset(dict_immutable.items())] = "new"
print(dict_immutable)
print('----------------------------')

# memorization (caching)
# dynamic programming
cache = {}

@lru_cache
def fib(n):
    if n in cache:
        return cache[n]
    elif n == 0:
        result = cache[n] = 0
    elif n == 1:
        result = cache[1] = 1
    else:
        result = cache[n] = fib(n - 1) - fib(n - 2)

    return result


# compute nth Fibonacci number:
fib(10)

print('cached fib result: ', cache)
print('----------------------------')

# functional programming principle:
# consider type safe
# what is type safe? inappropriate operations with types. i.e., divide a number by zero

# strongly typed language. every object / data has fixed type
print(type(3))
print(type("abc"))
print(type(numpy.array(['foo', 'boo', 'uoo'])))
print('----------------------------')

# dynamically typed. variable and functions do not have specified types. great for scripting but can cause errors
def func(x):
    return x * x

# x does not have a specified type
# therefore, when x = None passed, it will give an error

# statically typed language
# every variable and function has a specified type
def my_function(param1: List[int], params2: int) -> int:
    return param1[params2]

rt = my_function("xyz", 2) # <-- the compile will ignore the type hints
print(rt)
print(type(rt))
# any functional languages that have <type inference> where the compiler automatcially infers the types?
print('----------------------------')

# practice type safe when writing functuons with type safe langauge
def divide(x: int, y: int) -> int:
    if y == 0:
        return None
    else:
        return x // y

print("type safe divide function safegarud invalid input: ", divide(10, 0))
print("type safe divide function returns 2: ", divide(10, 5))
print('----------------------------')

# advantages of functional languages (why?)
# avoid null types (which we have to remember to handle)
# avoid raising errors (which we have to remember to handle)
# make sure one handles all possible cases (even rare ones)
# ensure that objects are only used in the way they were intended

# functional programming theory

# 1. product type: if A and B are types, so is the product of A x B
print('----------------------------')
print(type(3))
print(type(4))
print(type(3 * 4))
print('----------------------------')

# 2. function type: if A and B are types, A -> B is the type of function with A as input and B as output
print('----------------------------')

def add_two(x: int, y: int) -> int:
    return x + y

z = add_two(10, 33)

print("type of x + y with x & y both type int: ", type(z))
print('----------------------------')

# 3. sum type: if A and B are type, A | B is the type of objects of X where X is either type A or B
# this is not natrual in python
# advantage: allow more than one types for input but still have strict control over input types
# explore OCaml

# 4. recursive types
# it is self referential types naturally goes with recursive functions


if __name__ == "__main__":
    print("input is an integer: ", a)  # did not change
    print("input is an string: ", b)  # did not change
    print("input is a tuple: ", c)  # did not change
    print("input is a list of numbers: ", d)  # changed
    print("input is a boolean: ", e)  # did not change
    print("input is a float number: ", f)  # did not change
    print("input is a list of strings: ", g)  # changed
    print("input is a dict: ", h)  # operation did not work
    print("input is a set: ", i)  # no effet
    print("input is a numpy.array: ", j)  # changed
