# Any variable you create inside the class directly is treated as a
# common variable to all the objects of the class.
# Such variables are called as static variables.

class Spaceship:
    __no_of_passengers = 0  # static variables
    __no_of_engines = 0  # static variables
    __weight = 0  # static variables
    __country_of_made = None  # static variables

    def __init__(self, title, purpose):
        self.title = title
        self.purpose = purpose

    def info(self):
        return "Spaceship " + self.title + " is made to " + self.purpose

    def set_all_attributes(self):
        Spaceship.__no_of_passengers += 1
        Spaceship.__no_of_engines += 10
        Spaceship.__weight += 100
        Spaceship.__country_of_made = "Any"

    def get_all_attributes_via_obj_reference(self):
        return "this spaceship has " \
               + str(Spaceship.__no_of_passengers) \
               + " passengers, with " \
               + str(Spaceship.__no_of_engines) \
               + " engines and weigh " \
               + str(Spaceship.__weight) \
               + " lbs and is made in country of " \
               + str(Spaceship.__country_of_made)

    @staticmethod
    def get_all_attributes_static_method():
        return "this spaceship has " \
               + str(Spaceship.__no_of_passengers) \
               + " passengers, with " \
               + str(Spaceship.__no_of_engines) \
               + " engines and weigh " \
               + str(Spaceship.__weight) \
               + " lbs and is made in country of " \
               + str(Spaceship.__country_of_made)


# getting the static variables are not the right way
# using static methods are recommended
new_spaceship = Spaceship("red explorer", "navigate")
new_spaceship.set_all_attributes()
print("getting common variables set inside the class via obj ref: ",
      new_spaceship.get_all_attributes_via_obj_reference())
print("getting common variables set inside the class via static method: ", Spaceship.get_all_attributes_static_method())
print("----------------------")
another__new_spaceship = Spaceship("discover", "planetary exploration")
another__new_spaceship.set_all_attributes()
print("getting common variables set inside the class via obj ref: ",
      another__new_spaceship.get_all_attributes_via_obj_reference())
print("getting common variables set inside the class via static method: ", Spaceship.get_all_attributes_static_method())
