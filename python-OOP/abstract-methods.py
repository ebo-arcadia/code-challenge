# In OOP, we can create abstract methods. A class which has an abstract method cannot be instantiated.
# Similarly, a sub class of an abstract class cannot be instantiated unless it overrides the abstract method.

# abc - Abstract Base class
# ABCMeta - Inbuilt special class
# abstractmethod - Indicator to specify method is abstract.
from abc import ABCMeta, abstractmethod, ABC


class Person(metaclass=ABCMeta):
    @abstractmethod  # indicating the abstract methods
    def name(self):
        pass

    def age(self):
        return "I have an age because I am a person"

    def doing(self, action):
        return "doing" + action


class Dancer(Person):
    def name(self):
        return "I am a b-boy dancer!"


class Student(Person):
    def name(self):
        return "I am a student!"


class Traveler(Person):
    def name(self):
        return "I am a traveler"

    def age(self):
        return "I am 33 years ago"


dancerA = Dancer()
print("A dancer shout out: ", dancerA.name(), " and I am", dancerA.doing(" dancing on the floor with music"))
studentA = Student()
print("A new student says: ", studentA.name(), " and I am", studentA.doing(" studying in a coffee shop"))
travelerA = Traveler()
print("A travel just announced: ", travelerA.name(), " and I am", travelerA.age(), travelerA.doing(" and I am "
                                                                                                   "traveling across "
                                                                                                   "the "
                                                                                                   "country"))


# another example of multiple level inheritance implementation of abstract methods
class Machine(metaclass=ABCMeta):
    def __init__(self):
        self.software = "programming language"
        self.hardware = "metal"

    @abstractmethod
    def perform(self):
        return "hardware can perform tasks with software"


class Laptop(Machine):
    def __init__(self):
        super().__init__()
        self.brand = "pro16inch"


class MacBook(Laptop):
    def __init__(self):
        self.model = "Macbook pro 16 inch 2021"

    def perform(self):
        return "Macbook can be used to run python program"


class Cellphone(Machine):
    def featured(self, features):
        return "this cellphone has features of: " + features


macbook_obj = MacBook()
print("macbook obj perform: ", macbook_obj.perform())


# Another example of multi level inheritance implementation of abstract methods.
class Parent(metaclass=ABCMeta):
    def __init__(self):
        self.num = 5

    @abstractmethod
    def show(self):
        return "I am the show method in the Parent class"


class Child(Parent):  # Here we have not override the show method, but the GrandChild which is sub class for Child
    # overriden it.
    def __init__(self):
        super().__init__()
        self.var = 10


class GrandChild(Child):
    def show(self):  # This is where we override the show method of Parent class.
        print(self.num)
        print(self.var)
        print("This is possible")


obj = GrandChild()
obj.show()

