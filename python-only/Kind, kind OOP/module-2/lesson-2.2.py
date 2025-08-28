'''learning property'''
from tabnanny import check


class Person:
    def __init__(self, name: str, old: int):
        self.__name = name
        self.__old = old

    @property  #before the GETTER (!)
    def old(self):
        return self.__old

    @old.setter
    def old(self, old: int):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old

    # old = property() #its priority is higher than the local attributes' priority. only for the private and protected
    # old = old.setter(set_old)
    # old = old.getter(get_old)


# p = Person('john', 20)

# p.set_old(21)
# print(p.get_old())

# print(p.old)
# p.old = 21
# print(p.old)
# print(p.__dict__)


'''task1'''


class Car:
    def __init__(self):
        self.__model = None

    @staticmethod
    def __correct_parameters(model):
        return isinstance(model, str) and 2 <= len(model) <= 100

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model if self.__correct_parameters(model) else self.__model


'''task2'''


class WindowDlg:
    def __init__(self, title: str, width: int, height: int) -> None:
        self.__title = title
        self.__width = width
        self.__height = height

    @staticmethod
    def __size_check(number):
        return 0 <= number <= 10_000

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: int):
        if self.__size_check(width):
            self.__width = width
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: int):
        if self.__size_check(height):
            self.__height = height
            self.show()


'''task3'''


class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @staticmethod
    def check_next_value(value):
        return isinstance(value, StackObj) or value is None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class Stack:
    def __init__(self):
        self.top = None
        self.__objects = []

    def push(self, obj: StackObj):
        if self.top is None:
            self.top = obj
        else:
            self.__objects[-1].next = obj  #using setter, made with @property
        self.__objects.append(obj)

    def pop(self):
        flag = False
        if self.__objects:
            flag = True
            to_return = self.__objects.pop()
        if self.__objects:
            self.__objects[-1].next = None
        else:
            self.top = None
        return to_return if flag else None

    def get_data(self):
        return [object.data for object in self.__objects]


'''task4'''
class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.__x = 0
        self.__y = 0

        if self.__value_is_correct(x):  self.__x = x
        if self.__value_is_correct(y):  self.__y = y

    def __value_is_correct(self, value):
        return type(value) in (int, float) and self.MIN_COORD <= value <= self.MAX_COORD

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x if self.__value_is_correct(x) else self.__x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y if self.__value_is_correct(y) else self.__y

    @staticmethod
    def norm2(vector):
        return vector.x ** 2 + vector.y ** 2


'''task5 - unfinished'''
class TreeObj:
    def __init__(self, indx: int, value: str = None) -> None:
        self.__indx = indx
        self.__value = value
        self.__left = None
        self.__right = None


class DecisionTree:
    __INSTANCE = None

    def __new__(cls, *args, **kwargs):
        if cls.__INSTANCE is None:
            __INSTANCE = super().__new__(cls, *args, **kwargs)
            return __INSTANCE
        else:
            return cls.__INSTANCE

    @classmethod
    def predict(cls, root, x: list[int]):
        pass

    __objects = {}
    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        cls.__objects[node] = obj
        if left:
            node.left = obj
        else:
            node.right = obj


'''task6'''
import math


class LineTo:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y


class PathLines:
    def __init__(self, *args):
        if not args:
            self.__path = []
        else:
            self.__path = list(args)

    def get_path(self) -> list[LineTo]:
        return self.__path

    def get_length(self) -> int | float:
        total_length = 0
        if len(self.__path) == 1:
            total_length = math.sqrt(self.__path[0].x ** 2 + self.__path[0].y ** 2)
        if len(self.__path) > 1:
            total_length = math.sqrt(self.__path[0].x ** 2 + self.__path[0].y ** 2)
            for index, line in enumerate(self.__path):
                if index + 1 != len(self.__path):
                    total_length += math.sqrt((self.__path[index + 1].x - self.__path[index].x) ** 2 + (self.__path[index + 1].y - self.__path[index].y) ** 2)
        return total_length

    def add_line(self, line: LineTo) -> None:
        self.__path.append(line)


# p = PathLines(LineTo(10, 20), LineTo(10, 30))
# p.add_line(LineTo(20, -10))
# dist = p.get_length()
# print(dist)


'''task7'''
import re


class PhoneNumber:
    def __init__(self, number: int = 11_111_111_111, fio: str = "F I O") -> None:
        if self.__check_number(number): self.number = number
        if self.__check_fio(fio): self.fio = fio

    @staticmethod
    def __check_number(number: int) -> bool:
        return type(number) == int and re.fullmatch(r"^\d{11}$", str(number))

    @staticmethod
    def __check_fio(fio: str) -> bool:
        return type(fio) == str

class PhoneBook:
    def __init__(self) -> None:
        self.__phonebook = []

    def add_phone(self, phone):
        self.__phonebook.append(phone)

    def remove_phone(self, indx):
        self.__phonebook.pop(indx)

    def get_phone_list(self):
        return self.__phonebook