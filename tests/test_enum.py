from pyrp3.enum import Enum


def test_enum():
    class Color(Enum):
        RED = 1
        GREEN = 2
        blue = 3

    print(Color.red)

    print(repr(Color.red))
    print(Color.RED == Color.red)
    print(Color.RED == Color.blue)
    print(Color.RED == 1)
    print(Color.RED == 2)

    class ExtendedColor(Color):
        WHITE = 0
        ORANGE = 4
        YELLOW = 5
        PURPLE = 6
        BLACK = 7

    print(ExtendedColor.ORANGE)
    print(ExtendedColor.RED)

    print(Color.RED == ExtendedColor.RED)

    class OtherColor(Enum):
        WHITE = 4
        BLUE = 5

    class MergedColor(Color, OtherColor):
        pass

    print(MergedColor.RED)
    print(MergedColor.WHITE)

    print(Color)
    print(ExtendedColor)
    print(OtherColor)
    print(MergedColor)
