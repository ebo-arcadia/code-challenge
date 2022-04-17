import abc


class FlyingObject(metaclass=abc.ABCMeta):
    _flying_objects = []

    def __init__(self, name):
        self._in_air = False
        self.name = name
        type(self)._flying_objects.append(self)

    @abc.abstractmethod
    def take_off(self):
        self._in_air = True

    @abc.abstractmethod
    def land(self):
        self._in_air = False

    @classmethod
    def flying_objects(cls):
        return cls._flying_objects

    def __str__(self):
        return self.name


class Plane(FlyingObject):
    _planes = []
    _flying_objects = []

    def __init__(self, name):
        super().__init__(name)
        type(self)._planes.append(self)
        self._over_land = True

    @property
    def over_land(self):
        return self._over_land

    @over_land.setter
    def over_land(self, over_land):
        self._over_land = over_land

    def take_off(self):
        super().take_off()

    def land(self):
        if self.over_land:
            super().land()

    @classmethod
    def planes(cls):
        return cls._planes


class Bird(FlyingObject):
    _birds = []

    def __init__(self, name):
        super().__init__(name)
        type(self)._birds.append(self)
        self._healthy_wings = True

    def take_off(self):
        if self.healthy_wings:
            super().take_off()

    def land(self):
        super().land()

    @classmethod
    def birds(cls):
        return cls._birds

    @property
    def healthy_wings(self):
        return self._healthy_wings

    @healthy_wings.setter
    def healthy_wings(self, healthy):
        self._healthy_wings = healthy


if __name__ == "__main__":
    ufo = FlyingObject('UFO')
    print(ufo.flying_objects()[0])
    plane = Plane('Air Force One')
    print(plane.flying_objects()[0])
    bird_1 = Bird('anger bird')
    bird_1.take_off()
    bird_2 = Bird('yellow hawk')
    bird_2.take_off()
    print("bird 1:", bird_1, sep=" ")
    print("------------")
    print("bird 2:", bird_2, sep=" ")
