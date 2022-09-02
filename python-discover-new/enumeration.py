from enum import Enum
from typing import Tuple


class Engineering(Enum):
    civic = "city design"
    marine = "ocean"
    aerospace = "space shuttle"
    genetic = "DNA mapping"


print(Engineering.civic, Engineering.marine, Engineering.aerospace, Engineering.genetic, end="!!!")


class Painter(Enum):
    red = (1, (255, 0, 0), "#ff0000")
    green = (2, (128, 0, 0), "#008000")
    blue = (3, (0, 0, 255), "#00000ff")

    def __str__(self) -> str:
        return self.name.lower()

    def num(self) -> int:
        return self.value[0]

    def rgb(self) -> Tuple:
        return self.value[1]

    def hex(self) -> str:
        return self.value[2]

    def combine_color_with(self, other_color) -> str:
        if self.name == 'red':
            if other_color.name == 'blue':
                return "#800080"  # PURPLE
            elif other_color.name == 'green':
                return "#FFFF00"  # yellow

    @classmethod
    def default_color(cls):
        return cls.red


str(Painter.red)
print(Painter.default_color())
Painter.blue.num()
Painter.green.rgb()
Painter.red.combine_color_with(Painter.blue)

