# Python has a built method called __str__(self), which will called automatically when we print an object.
# __str__(self) must return a String, so for other datatypes we need to do type casting

class Country:
    def __init__(self):
        self.__name = None
        self.__region = None
        self.__established = None

    def set_name(self, country_name):
        self.__name = country_name

    def get_name(self):
        return self.__name

    def set_region(self, country_region):
        self.__region = country_region

    def get_region(self):
        return self.__region

    def set_established(self, year):
        self.__established = year

    def get_established(self):
        return self.__established

    @staticmethod
    def info():
        print("info static method")

    # __str__
    def __str__(self):
        return "country name is " \
               + self.__name \
               + " which is located in " \
               + self.__region \
               + " and it was founded in year " \
               + str(self.__established)


nation = Country()
nation.set_name("USA")
nation.set_region("North America")
nation.set_established(1784)
print(nation)
print(str(nation))
print(nation.__str__())
print(nation.__repr__())
