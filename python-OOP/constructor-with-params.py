# how to create a class with constructor
# how to instantiate an object using the class passing parameters
# difference among instance, static, class, and abstract methods


class Company:
    def __init__(self, industry, mission, established, location):
        self.industry = industry
        self.mission = mission
        self.established = established
        self.location = location

    # instance method
    def description(self):
        return "this statement is returned by an instance method called description"

    @classmethod
    # class method is often used to be called with the class name instead of the object
    # class method has access to the state of class and takes class parameters
    # class method points at the class, can modify the state of it and all instances from this class
    # class method can be used to create an object from a class
    def operations(cls, industry, mission, established, location):
        print("after an instance is instantiated using the operations class method, the following print is executed: ")
        print("industry of this company: ", industry, "location of this company: ", location)
        return cls(industry, mission, established, location)

    @staticmethod
    def info():
        print("industry: ", slack.industry, "mission: ", slack.mission, "established: ", slack.established, "location: ",
              slack.location)
        return "this is returned by a static method"


# instantiate an object
slack = Company("communication", "improve workflow efficiency", "2000", "San Francisco")
print("object slack calling static method defined in the class: ", slack.info())

# instantiate an object with class method
apple = Company.operations("tech", "enrich lives", "1970", "mountain view")
apple_industry = apple.industry
apple_location = apple.location
print("object apple instantiated with class: ", apple_industry, apple_location)
print("instance calling instance method defined in the class: ", slack.description())