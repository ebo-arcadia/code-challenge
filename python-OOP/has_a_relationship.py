# In Object Oriented Approach, it is possible to have relationships between classes. When an object of a class
# becomes the instance variable of another class, it is known as "has-a" relationship or AGGREGATION. If ClassA
# 'has-a' ClassB, then ClassB aggregates ClassA


class House:
    def __init__(self, address, rent, renter):
        self.address = address
        self.rent = rent
        self.tenant = renter  # instance variable of another class is passed


class Tenant:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


tenantA = Tenant("John", 50000)
house = House("1610 BayRidge", 1200, tenantA)
print("house obj address: ", house.address)
print("house obj rent: ", house.rent)
print("house obj tenant name: ", house.tenant.name)
print("house obj tenant salary: ", house.tenant.salary)

tenantB = Tenant("Patrik", 100000)
house = House("1010 Bush St", 900, tenantB)
print("house obj address: ", house.address)
print("house obj rent: ", house.rent)
print("house obj tenant name: ", house.tenant.name)
print("house obj tenant salary: ", house.tenant.salary)
