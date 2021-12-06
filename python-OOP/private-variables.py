# Variables which should not be accessed outside a class are called private variables.
# In Python you can easily create private variables by prefixing it with a double underscore ( __ )

# Whenever you create a private variable, python internally changes its name as _ClassName__variableName.

# Methods used to set values are called as 'mutator' methods and methods used to get values are called as 'accessor'
# methods! why private variable and what is the benefit or use of it? it is perhaps culture and to warn others to not
# touch these variables even technically one can


class Person:
    def __init__(self, name):
        self.name = name
        self.__religious_belief = None
        self.__faith = None
        self.__age = 0

    def set_private_attr(self, religion, faith, age):  # mutator method
        self.__religious_belief = religion
        self.__faith = faith
        self.__age = age

    def get_private_attr(self):  # accessor method
        return self.name \
               + " is " \
               + str(self.__age) \
               + " years old" \
               + " with a faith in " \
               + self.__faith \
               + " and practice " \
               + self.__religious_belief \
               + " religion"

    def __str__(self):
        return "Private attributes __religious_belief: " \
               + self.__religious_belief \
               + ". Private attributes __faith: " \
               + self.__faith \
               + ". Private attribute age: " \
               + str(self.__age)


person_a = Person("Peterson")
# using mutator method to set private attributes
person_a.set_private_attr("methodist", "God", 65)
# using accessor method to get private attributes
result = person_a.get_private_attr()
print("private attributes of set by person_a: ", result)
print("convert obj person_b to string: ", person_a.__str__())

print("-----------------------------")

person_b = Person("Jonna")
# set private variable using obj._Person__religious_belief but this is not the recommended way
person_b._Person__religious_belief = "Baptism"
person_b._Person__faith = "poly"
person_b._Person__age = 18
print("convert obj person_b to string: ", person_b.__str__())

