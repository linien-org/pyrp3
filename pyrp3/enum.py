"""Enumeration metaclass."""


class EnumMetaclass(type):
    """Metaclass for enumeration.

    To define your own enumeration, do something like

    class Color(Enum):
        red = 1
        green = 2
        blue = 3

    Now, Color.red, Color.green and Color.blue behave totally different: they are
    enumerated values, not integers. Enumerations cannot be instantiated; however they
    can be subclassed.
    """

    def __init__(cls, name, bases, dict):
        super(EnumMetaclass, cls).__init__(name, bases, dict)
        cls._members = []
        cls._reverse_dct = {}
        for attr in list(dict.keys()):
            if not (attr.startswith("__") and attr.endswith("__")):
                enumval = EnumInstance(name, attr, dict[attr])
                setattr(cls, attr, enumval)
                cls._members.append(attr)
                cls._reverse_dct[dict[attr]] = enumval

    def __getattr__(cls, name):
        if name == "__members__":
            return cls._members
        raise AttributeError(name)

    def __repr__(cls):
        s1 = s2 = ""
        enumbases = [
            base.__name__
            for base in cls.__bases__
            if isinstance(base, EnumMetaclass) and base is not Enum
        ]
        if enumbases:
            s1 = "(%s)" % ", ".join(enumbases)
        #        enumvalues = ["%s: %d" % (val, getattr(cls, val))
        enumvalues = [
            "%s: %d" % (getattr(cls, val), getattr(cls, val)) for val in cls._members
        ]
        if enumvalues:
            s2 = ": {%s}" % ", ".join(enumvalues)
        return "%s%s%s" % (cls.__name__, s1, s2)

    def __call__(cls, key=None):
        if key is None:
            return cls
        if key in cls._members:
            return getattr(cls, key)
        return cls._reverse_dct[int(key)]


class EnumInstance(int):
    """Class to represent an enumeration value.

    EnumInstance('Color', 'red', 12) prints as 'Color.red' and behaves like the integer
    12 when compared, but doesn't support arithmetic.

    XXX Should it record the actual enumeration rather than just its name?
    """

    def __new__(cls, classname, enumname, value):
        return int.__new__(cls, value)

    def __init__(self, classname, enumname, value):
        self.__classname = classname
        self.__enumname = enumname

    def __repr__(self):
        return "EnumInstance(%s, %s, %d)" % (self.__classname, self.__enumname, self)

    def __str__(self):
        return "%s.%s" % (self.__classname, self.__enumname)


class Enum(metaclass=EnumMetaclass):
    pass
