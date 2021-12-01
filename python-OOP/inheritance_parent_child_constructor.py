# In python inheritance, when an object of child class is created,
# the parent class constructor is called only if the child class
# does not have its own constructor.Else the parent class constructor is not called.

# To invoke the parent class constructor and methods, we can use a magic method called super()


class BigBoss:
    def __init__(self, name, title, duty, skill):
        self.name = name
        self.title = title
        self.duty = duty
        self.skill = skill

    @staticmethod
    def boss_move():
        return "boss is taking action!"

    @classmethod
    def get_boss(cls, name, skill):
        result = name + " is using " + skill
        return result


class Boss(BigBoss):
    def __init__(self, name, title, duty, skill, unique, only_boss):
        super().__init__(name, title, duty, skill)  # invoke BigBoss constructor
        self.unique = unique
        self.only_boss = only_boss


class Snake(Boss):
    def __init__(self, name, title, duty, skill, unique, only_boss):
        super().__init__(name, title, duty, skill, unique, only_boss)  # invoke Boss constructor
        self.name = name
        self.title = title
        self.duty = duty
        self.skill = skill
        self.unique = unique
        self.only_boss = only_boss


print(BigBoss.boss_move())
print(BigBoss.get_boss("Liquid Snake", "shooting missiles"))

boss_obj = Boss("snake", "hero", "save the world", "infiltrate", "boss is snake and big boss is his mentor",
                "attribute only in Boss")
print(boss_obj.name)
print(boss_obj.title)
print(boss_obj.duty)
print(boss_obj.skill)
print(boss_obj.unique)
print(boss_obj.only_boss)
print(boss_obj.boss_move())
print(boss_obj.get_boss("Solid Snake", "CQC"))

snake_obj = Snake("solid snake", "the sorrow hero", "destroy the nuclear bomb", "CQC", "Solid Snake has his own "
                                                                                       "uniqueness", "attribute only "
                                                                                                     "for Snake")
print(snake_obj.unique)
print(snake_obj.only_boss)
