# Defining a class
# Always remember that in a method since 'self' is not a keyword, no matter what variable is used,
# the first parameter is always considered as the implicit reference to the object used.
class Family:
    # constructor method to instantiate objects
    def __init__(self):
        # create properties for the class
        self.name = None
        self.gender = None
        self.role = None
        self.age = None

    def duty(self):
        if self.role == "father":
            return "father symbolizes discipline and truth"
        if self.role == "mother":
            return "mother symbolizes kindness and goodness"


dad = Family()
dad.name = "Sega"
dad.gender = "male"
dad.role = "father"
dad.age = "33"

print("family member's name: ", dad.name)
print("family member's gender: ", dad.gender)
print("family member's title: ", dad.role)
print("family member's age: ", dad.age)
print(dad.duty())




