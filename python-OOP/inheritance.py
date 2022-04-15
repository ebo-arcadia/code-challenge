from collections import Counter


class SuperClass:
    def __init__(self, name, funds):
        self.name = name
        self.funds = funds

    def intro(self):
        print('Hello, my name is {} and I come from the SUPER CLASS'.format(self.name))

    def outro(self):
        print('Goodbye!')

    def get_all_funds(self):
        print('this method returns all {}'.format(self.funds))


class SubClass(SuperClass):
    def intro(self):
        print('hey there, my name is {} and I come from the SUB CLASS'.format(self.name))

    def get_all_funds(self):
        super().get_all_funds()
        print("...and more!")


superman = SuperClass("superman", "benchmarks")
sub = SubClass("human", "S&P500")

print("------", sep="")
superman.intro()
superman.outro()
superman.get_all_funds()
print("------", sep="")
sub.intro()
sub.outro()
sub.get_all_funds()
print("------", sep="")


# built-in list class provides a built-in method append
# how to build a prepend method?


class MyList(list):
    def prepend(self, obj):
        self.insert(0, obj)


myList = MyList(['x', 'y', 'z'])
myList.append('@')
myList.prepend('alpha')
print(myList)
print("------", sep="")


class NonNegativeCounter(Counter):
    """Counter that disallows negative values using inheritance and method override"""

    def __setitem__(self, key, value):
        value = 0 if value < 0 else value
        super().__setitem__(key, value)


# implementing the above class
count_items_dict = ['green', 'blue', 'blue', 'red', 'yellow', 'green', 'blue']
counter = NonNegativeCounter(count_items_dict)
print("initial count of all colors: ")
print(counter)
print("------", sep=" ")
counter.subtract(['red', 'yellow', 'green', 'blue', 'red', 'yellow', 'green', 'blue', 'red', 'yellow', 'green', 'blue'])
print("count of all colors after subtraction: ")
print(counter)
print("------", sep=" ")


# using static method
# why use it? what are the common use case?
# what is the difference between regular method and static method?
# how and when to use it in my work?

class Triangle:
    def __init__(self, sides):
        if not self.is_triangle(sides):
            raise Exception('Cannot make triangle with those sides.')
        self._sides = sides

    @property
    def perimeter(self):
        return sum(self._sides)

    @property
    def area(self):
        p = self.perimeter / 2
        a = self._sides[0]
        b = self._sides[1]
        c = self._sides[2]
        return (p * (p - a) * (p - b) * (p - c)) ** .5

    @staticmethod
    def is_triangle(sides):
        if len(sides) != 3:
            return False
        sides.sort()
        if sides[0] + sides[1] < sides[2]:
            return False
        return True


# implementing code above
good = [3, 3, 5]
bad = [3, 3, 9]
eval_without_obj_self = Triangle.is_triangle(good)
print(eval_without_obj_self, sep=" ")
print("--------")
eval_without_obj_self = Triangle.is_triangle(bad)
print(eval_without_obj_self, sep=" ")
print("--------")
triangle1 = Triangle(good)
print("evaluate with triangle object:", sep=" ")
print(triangle1.area, sep=" ")
print("--------")
triangle2 = Triangle(bad)
print("evaluate with triangle object:", sep=" ")
print(triangle2.area, sep=" ")
print("--------")



