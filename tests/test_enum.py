from pyrp3.enum import Enum


def test_enum():
    class Color(Enum):
        red = 1
        green = 2
        blue = 3

    print(Color.red)

    print(repr(Color.red))
    print(Color.red == Color.red)
    print(Color.red == Color.blue)
    print(Color.red == 1)
    print(Color.red == 2)

    class ExtendedColor(Color):
        white = 0
        orange = 4
        yellow = 5
        purple = 6
        black = 7

    print(ExtendedColor.orange)
    print(ExtendedColor.red)

    print(Color.red == ExtendedColor.red)

    class OtherColor(Enum):
        white = 4
        blue = 5

    class MergedColor(Color, OtherColor):
        pass

    print(MergedColor.red)
    print(MergedColor.white)

    print(Color)
    print(ExtendedColor)
    print(OtherColor)
    print(MergedColor)
