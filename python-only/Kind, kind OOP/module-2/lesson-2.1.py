'''ENCAPSULATION'''
from typing import Any


class Point1:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y


# pt1 = Point1(1, 2)
# pt1.x = 100
# pt1.y = "coord_y"
# print(pt1.x, pt1.y)


'''learning protected'''
class Point2:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self._x = x
        self._y = y


# pt2 = Point2(1, 2)
# pt2._x = 200
# pt2._y = "coord_y"
# print(pt2._x, pt2._y)


'''learning private'''
'''learning protected'''
class Point3:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.__x = self.__y = 0
        if self.__is_number(x) and self.__is_number(y):
            self.__x = x
            self.__y = y

    @classmethod
    def __is_number(cls, x) -> bool:
        return type(x) in (int, float)

    def set_coords(self, external_value) -> None: #setter
        if self.__is_number(external_value):
            self.__x = external_value
            self.__y = external_value

    def get_coords(self) -> None:   #getter
        print((self.__x, self.__y))


pt3 = Point3(1, 2)
def tests_pt3(pt3: Point3) -> None:
    pt3.__x = 300
    pt3.__y = "coord_y"
    try:
        print(pt3.__x, pt3.__y)
    except AttributeError:
        print(f"(!) cannot edit private variable. using Point3.set_coords(10) you can get __x = 10, __y = 10")
    pt3.get_coords()    #using getter
    pt3.set_coords(10) #using setter
    pt3.get_coords()    #using getter again
    print(pt3.__dict__, f'I have got it! __x == {pt3._Point3__x}') #needs accessify.private


'''task1'''
class Clock:
    def __init__(self, tm=0):
        if self.__check_time(tm):
            self.__time = tm

    @classmethod
    def __check_time(cls, tm: int) -> bool:
        return type(tm) == int and 0 <= tm <= 100_000

    def set_time(self, tm: int) -> int:
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self) -> int:
        return self.__time


clock = Clock(4530)


'''task2'''
class Money:
    def __init__(self, money: int) -> None:
        self.__money = money

    @classmethod
    def __check_money(cls, money: int) -> bool:
        return type(money) == int and 0 <= money

    def set_money(self, money: int) -> None:
        self.__money = money if self.__check_money(money) else self.__money

    def get_money(self) -> int:
        return self.__money

    def add_money(self, mn) -> None:
        self.__money += mn.get_money()


'''task3'''
class Book:
    def __init__(self, author: str, title: str, price: int) -> None:
        self.__author = author
        self.__title = title
        self.__price = price

    def set_title(self, title: str) -> None:
        self.__title = title

    def set_author(self, author: int) -> None:
        self.__author = author

    def set_price(self, price: int) -> None:
        self.__price = price

    def get_title(self) -> str:
        return self.__title

    def get_author(self) -> str:
        return self.__author

    def get_price(self) -> int:
        return self.__price


'''task4'''
class Line:
    def __init__(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def set_coords(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_coords(self) -> tuple[int, int, int, int]:
        return (self.__x1, self.__y1, self.__x2, self.__y2)

    def draw(self) -> None:
        print(*self.get_coords())


'''task5'''
class Point:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.__x = x
        self.__y = y

    def get_coords(self) -> tuple[int, int]:
        return (self.__x, self.__y)


class Rectangle:
    def __init__(self, *args) -> None:
        if len(args) == 2 and all([isinstance(elem, Point) for elem in args]):
            self.__sp, self.__ep = args
        else:
            self.__sp, self.__ep = Point(args[0], args[1]), Point(args[0], args[1])

    def set_coords(self, sp, ep) -> None:
        self.__sp = sp
        self.__ep = ep

    def get_coords(self) -> tuple[Point, Point]:
        return self.__sp, self.__ep

    def draw(self) -> None:
        print(f"Прямоугольник с координатами: ({', '.join(map(str, self.__sp.get_coords()))}) ({', '.join(map(str, self.__ep.get_coords()))})")


'''task6'''
class ObjList:
    def __init__(self, data: str) -> None:
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, next) -> None:
        self.__next = next

    def set_prev(self, prev) -> None:
        self.__prev = prev

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data) -> None:
        self.__data = data

    def get_data(self) -> list:
        return [elem.get_data() for elem in self.__data]

class LinkedList:
    def __init__(self):
        self.__data = []
        self.head = None
        self.tail = None

    def add_obj(self, obj: ObjList) -> None:
        if self.__data:
            obj.set_prev(self.__data[-1])
            self.__data[-1].set_next(obj)
        else:
            self.head = obj
        self.tail = obj
        self.__data.append(obj)

    def remove_obj(self) -> None:
        self.__data[-1].set_prev(None)
        self.__data.pop()
        if self.__data:
            self.__data[-1].set_next(None)
            self.tail = self.__data[-1]
        else:
            self.head = None
            self.tail = None

    def get_data(self) -> list:
        return self.__data


'''task7'''
import random
import re


class EmailValidator:
    def __new__(cls, *args, **kwargs):
        cls.__email = None
        return None

    @staticmethod
    def __is_email_str(email) -> bool:
        return isinstance(email, str)

    @classmethod
    def get_random_email(cls):
        accessible_symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_."
        cls.__email = f'{random.choice(accessible_symbols) * random.randint(1, 100)}@{random.choice(accessible_symbols) * random.randint(1, 50)}'

        double_point = []
        for index, symbol in enumerate(cls.__email):
            if symbol == '.' and index != len(accessible_symbols) - 1 and cls.__email[index + 1] == '.':
                double_point.append(index)
        for index in double_point:
            cls.__email = f"{cls.__email[:index]}{random.choice(accessible_symbols[:-1])}{cls.__email[index + 1:]}"

        cat_index = cls.__email.index('@')
        if not '.' in cls.__email[cat_index + 1:]:
            domain_name_length = len(cls.__email[cat_index + 1:])
            domain_point_index = random.randint(cat_index + 1, cat_index + 1 + domain_name_length)
            cls.__email = f"{cls.__email[:domain_point_index]}.{cls.__email[domain_point_index + 1:]}"

        return cls.__email

    @classmethod
    def check_email(cls, email: str) -> bool:
        if cls.__is_email_str(email):
            if re.match(r'[a-zA-Z\d_\.]{1,100}@[a-zA-Z\d_\.]{1,50}', email) and '.' in email[email.find('@'):] and '..' not in email:
                return True
        return False