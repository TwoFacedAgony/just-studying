class Point3D:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("coord must be int")

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self.verify_coord(value)
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self.verify_coord(value)
        self._y = value

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self.verify_coord(value)
        self._z = value


# p = Point3D(1, 2, 3)
# print(p.__dict__)


class Integer:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("coord must be int")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        print(f"__set__: {self.name} = {value}")
        setattr(instance, self.name, value)


class Point4D:
    x1 = Integer()
    x2 = Integer()
    x3 = Integer()
    x4 = Integer()

    def __init__(self, x1, x2, x3, x4):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4


p4 = Point4D(1, 2, 3, 4)
p4.__dict__
