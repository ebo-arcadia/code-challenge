# the functools is a collection of higher-order functins
# a higher-order function takes another function as a paramter
# it can also return a function as its value from another function

# three most useful functions in the functools package
# 1. total ordering decorator
# it is used mostly for object comparison
# instead of manually define functions for <, <=, =, >, =>, with two functions defined, all others are provided
import itertools
from functools import total_ordering
from functools import reduce
from functools import partial

# define an order-able class using the total_ordering decorator
@total_ordering
class Car:
    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color

    def __eq__(self, other):
        return self.year == other.year

    def __gt__(self, other):
        return self.year > other.year

    def __repr__(self):
        return self.brand + self.color + str(self.year)


cars = [Car("Honda", 1999, "black"), Car("Toyota", 2000, "Gold"), Car("Benz", 2021, "silver"),
        Car("Tesla", 2020, "Green"), Car("BMW", 2031, "blue"), Car("Volvo", 2022, "White")]
print(cars)

# 2: reduce
# it is function reduce a sequence such as a list to a single value
# it takes two parameters, firs a function, second a sequence
# reduce applies the function to every sequence till the singel value is returned

# example 1
def reduce_to_sum(a_list_of_nums):
    return reduce(lambda x,y: x + y, a_list_of_nums)

# example 2
print("return car with latest year: ", reduce(lambda car1, car2: car1 if (car1 > car2) else car2, cars))

# 3: partial
# the concept of partial is to create new functions from existing functions by fixing few function arguments
# what is partial objects? callable objects created by functools.partial()
# key attributes: partial.func; partial.args; partial.keywords

# example 1
def times_two_nums(a, b):
    return a * b

partial_times_two_nums = partial(times_two_nums, 10)

# example 2
# given a list of names, generate another list of emails with the names appended to the front using partial

def email_maker(names, domain):
    list_of_names = []
    for name in names:
        name += domain
        list_of_names.append(name)
    return list_of_names


names = ["John", "Bob", "Tom", "Jame", "Peter"]
print(email_maker(names, "@gmail.com"))


if __name__ == "__main__":
    # compare cars by year
    # less than
    print(Car("Honda", 2000, "black") < Car("Toyota", 2001, "Gold"))

    # equal to
    print(Car("Benz", 2021, "silver") == Car("Tesla", 2021, "Green"))

    # greater than
    print(Car("BMW", 2031, "blue") > Car("Volvo", 2022, "White"))

    print("--------------------")

    print("add all nums in a list using reduce: ", reduce_to_sum([1, 2, 3, 5, 9]))

    print("--------------------")
    print("partial func supplied with arg 10 prepend to the left and keyword 11: ", partial_times_two_nums(11))

    print("--------------------")
    gmail_maker = partial(email_maker, domain="@gmail.com")
    print("partial func gmail maker returns a list of g-mails: ", gmail_maker(names))


