# Defining a class
class Family:
    # constructor method to instantiate objects
    def __init__(self):
        # create properties for the class
        self.name = None
        self.gender = None
        self.title = None
        self.age = None


dad = Family()
dad.name = "Sega"
dad.gender = "male"
dad.title = "father"
dad.age = "33"

print("family member's name: ", dad.name)
print("family member's gender: ", dad.gender)
print("family member's title: ", dad.title)
print("family member's age: ", dad.age)

