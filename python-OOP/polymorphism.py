# Polymorphism - One method can have different versions.
# We can override the methods of parent class in the child class.
# The method to be called is decided automatically depending on the object on which the method is invoked.

class Human:
    def eat(self, food):
        return "class Human method eat what food: " + food

    def sleep(self, hours):
        return "class human method sleep for how long: " + str(hours) + " hours"


class Engineer(Human):
    def eat(self, food):
        return "class Engineer method eat specific food: " + food  # eat method is overridden

    def work(self, task):
        return "class Enginner method work perform what task: " + task


class Police(Human):
    def salary(self, salary):
        return "class Police method salary gets paid for: " + str(salary)


class Developer(Engineer):
    def skill(self, skill):
        return "class Developer method skill which a developer normally acquire: " + skill


engineer = Engineer()
print(engineer.eat("avocado"))
print(engineer.sleep(8))
print(engineer.work("making software"))
print("-------------------")
policeman = Police()
print(policeman.eat("burger"))
print(policeman.sleep(7))
print(policeman.salary(100000))
print("-------------------")
developer = Developer()
print(developer.eat("cheese"))
print(developer.sleep(10))
print(developer.work("make website"))
print(developer.skill("make frontend UI"))
