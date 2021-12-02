# Types of inheritance
# 1. Single-level Inheritance
# 2. Multi-level Inheritance
# 3. Heirarchical Inheritance
# 4. Multiple Inheritance

class Creation:
    def __init__(self, species):
        self.species = species

    def feature(self):
        species = self.species
        return species + "can perform certain functions"


class Human(Creation):
    def living(self):
        species = self.species
        return species


person = Human("homo sapiens")
print(person.species)
print(person.feature())
