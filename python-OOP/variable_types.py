# Instance Variable	- attributes can be instantiated using the constructor in a class
# Reference Variable - object created as a reference variable refers to the class the object is created from
# Local Variable - variables created when a method in the class object is invoked on an object created from this class

class Property:
    def __init__(self):
        self.no_of_bedroom = 0  # instance variable
        self.no_of_bathroom = 0  # instance variable
        self.price = 0  # instance variable
        self.monthly_payment = 0  # instance variable
        self.rent = 0  # instance variable
        self.property_type = None  # instance variable
        self.good_neighborhood = None  # instance variable

    def rank(self):
        if self.good_neighborhood and self.property_type == "single family house":
            rank = "prime"  # local variable
        elif 150000 <= self.price <= 180000 and self.rent - self.monthly_payment >= 800:
            rank = "secondary"  # local variable
        else:
            rank = "no good and pass"  # local variable
        return rank


house_a = Property()  # house_a is a reference variable refers to the class Property
house_a.no_of_bedroom = 3
house_a.no_of_bedroom = 2
house_a.price = 175000
house_a.monthly_payment = 800
house_a.rent = 1800
house_a.property_type = "single family house"
house_a.good_neighborhood = True
print("rank of house_a: ", house_a.rank())

print("------------------------")
house_b = Property()  # house_b is a reference variable refers to the class Property
house_b.no_of_bedroom = 4
house_b.no_of_bedroom = 2
house_b.price = 167000
house_b.monthly_payment = 600
house_b.rent = 1800
house_b.property_type = "townhouse"
house_b.good_neighborhood = False
print("rank of house_b: ", house_b.rank())

print("------------------------")
house_c = Property()  # house_c is a reference variable refers to the class Property
house_c.no_of_bedroom = 2
house_c.no_of_bedroom = 1
house_c.price = 200000
house_c.monthly_payment = 900
house_c.rent = 1200
house_c.property_type = "townhouse"
house_c.good_neighborhood = False
print("rank of house_c: ", house_c.rank())
