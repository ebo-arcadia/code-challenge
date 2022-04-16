# what is class attribute and what is instance attribute?
# what are the differences and what are use case for each?
class Animal:
    type = "living being"
    function = "live"
    features = ["legs or no", "skins", "reproduction", "senses"]
    count = 1

    def __init__(itself):
        itself.function = "eat"
        itself.features = ["bark", "play", "4 legs"]
        itself.features.append('genetically added features?')

    @classmethod
    def increment_to_count(cls):
        cls.count += 1
        print(cls.count)


dog = Animal()
print(Animal.type, Animal.function, dog.type, dog.function)
print("--------")
print("executing code for using instant or class attributes:", sep=" ")
print(Animal.features)
print(dog.features)
print("--------")

print("executing code for using class method:", sep=" ")
print("class calls the class method: ")
Animal.increment_to_count()

print("--------")
print("instance calls the class method: ")
animal_a = Animal()
animal_a.increment_to_count()

print("--------")
print(" another instance calls the class method: ")
animal_b = Animal()
animal_b.increment_to_count()

print("--------")
print("class calls the class method again: ")
Animal.increment_to_count()


# when to use class attributes and methods?
# a use case: track how many planes are in the air and landed

class Plane:
    planes = []

    def __init__(self):
        self._in_air = False
        type(self).planes.append(self)

    def take_off(self):
        self._in_air = True

    def land(self):
        self._in_air = False

    @classmethod
    def num_planes(cls):
        print(len(cls.planes))

    @classmethod
    def num_planes_in_air(cls):
        return len([plane for plane in cls.planes if plane._in_air])


print("-------------")
# execute plane tracking code above
plane1 = Plane()
plane2 = Plane()
plane3 = Plane()
plane4 = Plane()
plane1.take_off()
plane2.take_off()
plane3.take_off()
plane4.take_off()
print("expecting 4 planes took off in the air", sep="")
print("-------------")
print(Plane.num_planes(), Plane.num_planes_in_air())
print("-------------")

plane1.land()
plane2.land()
print("expecting 2 planes are in the air after two landed", sep="")
print("-------------")
print(Plane.num_planes(), Plane.num_planes_in_air())
print("-------------")


class Jet(Plane):

    def __init__(self):
        super().__init__()
        self.planes = []
        type(self).planes.append(self)


plane5 = Jet()
plane5.take_off()
print("expecting more planes in the air using sub class", sep="")
print("-------------")
print(Plane.num_planes(), Plane.num_planes_in_air())
print("-------------")

