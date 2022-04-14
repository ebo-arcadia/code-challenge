import math


class Circle:
    def __init__(self, val, prop='r'):
        """Create a circle based on a radius, diameter, circumference, or area
        Keyword arguments:
        val (float) --the value of prop prop (str)
        --'r' : radius (default) --'d' : diameter
        --'c' : circumference --'a' : area
        """
        if prop == 'r':
            self.set_radius(val)
        elif prop == 'd':
            self.set_diameter(val)
        elif prop == 'c':
            self.set_circumference(val)
        elif prop == 'a':
            self.set_area(val)
        else:
            raise Exception('prop must be r, d, c, or a')

    def set_radius(self, r):
        """sets _radius, _diameter, _circumference, and _area of circle object"""
        self._radius = r
        self._diameter = r * 2
        self._circumference = r * 2 * math.pi
        self._area = r ** 2 * math.pi

    def get_radius(self):
        return self._radius

    def set_diameter(self, d):
        self.set_radius(d / 2)

    def get_diameter(self):
        return self._diameter

    def set_circumference(self, c):
        self.set_radius(c / (2 * math.pi))

    def get_circumference(self):
        return self._circumference

    def set_area(self, a):
        self.set_radius((a / math.pi) ** .5)

    def get_area(self):
        return self._area

    def resize_by(self, amount):
        r = self._radius * (1 + amount)
        self.set_radius(r)


class School:
    def __init__(self):
        self._name = None
        self._ranking = None

    def get_school_name(self):
        return self._name

    def set_school_name(self, name):
        self._name = name

    school_property = property(get_school_name, set_school_name)

    @property
    def ranking(self):
        return self._ranking

    @ranking.setter
    def set_ranking(self, ranking):
        self._ranking = ranking


class Person:
    def __init__(self):
        self._name = None

    @property
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


person = Person()
person.set_name("Jeffrey")
print(person.get_name)







