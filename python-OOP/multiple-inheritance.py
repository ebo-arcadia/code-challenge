# Python allows a class to inherit multiple classes. This is also called as "Multiple Inheritance".
# Here the Dog class inherits both Animal and Pet class.
# When both the parent classes have same variables or methods, the class is determined from left to right.
# For example, in Dog(Animal, Pet): the methods are considered from left to right.
# That means if a method is not there in Animal class, only then it checks in the Pet class.
# Hence tommy.eat() would invoke Animal class eat method


# example without attributes
class Aircraft:
    def fly(self):
        return "Aircraft can fly"
    def landing(self):
        return "Aircraft lands on the ground"


class Airplane:
    def fly(self):
        return "Airplane can fly in the sky"
    def landing(self):
        return "Airplane usually lands in an airport"
    def depart(self):
        return "Airplane usually departs on time"


class Jet(Aircraft, Airplane):
    pass


united_airline = Jet()
print(united_airline.fly())
print(united_airline.landing())
print(united_airline.depart())

# example with attributes


class Company:
    def __init__(self, name, size, service):
        self.name = name
        self.size = size
        self.service = service

    def occupation(self):
        company_name = self.name
        company_size = self.size
        company_service = self.service
        return "occupation method in class Company: " + company_name + " is a " + company_size + " company which " \
                                                                                                      "provides " + \
               company_service + " service. "

    def info(self):
        return "Info method called from class Company."


class Organization:
    def __init__(self, name, size, service):
        self.name = name
        self.size = size
        self.service = service

    def occupation(self):
        company_name = self.name
        company_size = self.size
        company_service = self.service
        return "occupation method in class Organization: " \
               + "Company " + company_name \
               + " is a " + company_size \
               + " company which provides " \
               + company_service \
               + " service. "

    @staticmethod
    def info():
        return "info method called from class Organization"

    @staticmethod
    def about():
        return "about method called from class Organization"


class Institution(Company, Organization):
    def __init__(self, name, size, service):
        self.name = name
        self.size = size
        self.service = service
        # self.location = location


institution = Institution("FastLab", "startup", "automation")
print(institution.occupation())
print(institution.info())
print(institution.about())

