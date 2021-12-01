# Python allows you to create attributes dynamically as well. Whenever you try to assign a value to an attribute,
# it checks if the attribute is already present. If present, the attribute is assigned, else the attribute is created!

class Computer:
    def __init__(self):
        self.software = None
        self.hardware = None
        self.price = None

    def make_computer(self, software, hardware, price, brand):
        self.software = software
        self.hardware = hardware
        self.price = price
        self.brand = brand  # create individual attributes for obj. this is not encouraged


apple = Computer()
apple.make_computer("macOS", "macbook", 1000, "apple")
print(apple.software)
print(apple.hardware)
print(apple.price)
print(apple.brand)
