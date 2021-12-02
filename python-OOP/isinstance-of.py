# isinstance(obj, classinfo) is a built-in function in Python which returns true if argument obj is an object of
# argument classinfo. Else, it returns false.

class Machine:
    def __init__(self, name, function):
        self.name = name
        self.function = function


class School:
    def __init__(self, level, size):
        self.level = level
        self.size = size


class Home:
    def __init__(self, feature, price):
        self.feature = feature
        self.price = price


m1 = Machine("car", "commute")
m2 = Machine("airplane", "fly")
s1 = School("elementary", "small")
s2 = School("university", "large")
h1 = Home("single family", 150000)

list_objs = [m1, m2, s1, s2]
for obj in list_objs:
    if isinstance(obj, Machine):
        print("obj m name: ", obj.name, "; obj m function: ", obj.function)
    if isinstance(obj, School):
        print("obj s level: ", obj.level, "; obj s1 size: ", obj.size)

print("is object h1 an instance of the Machine class? ", isinstance(h1, Machine))
