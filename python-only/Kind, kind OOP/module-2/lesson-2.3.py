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


# p4 = Point4D(1, 2, 3, 4)
# p4.__dict__


'''task1'''
class FloatValue:
    @classmethod
    def verify_value(cls, value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_value(value)
        setattr(instance, self.name, value)


class Cell:
    value = FloatValue()

    def __init__(self, value = 0.0) -> None:
        self.value = value

class TableSheet:
    def __init__(self, N: int, M: int) -> None:
        self.cells = [[Cell() for _ in range(M)] for _ in range(N)]


# table = TableSheet(5, 3)
# cell_number = 1.0
# for line_index, line in enumerate(table.cells, start=0):
#     for cell_index, cell in enumerate(line, start=0):
#         line[cell_index].value = cell_number
#         cell_number += 1.0
#
# for line_index, line in enumerate(table.cells, start=0):
#     for cell_index, cell in enumerate(line, start=0):
#         print(line[cell_index].x)


'''task2'''
class ValidateString:
