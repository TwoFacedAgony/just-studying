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

    def __set_name__(self, owner, name):    #sets the self.name = '_{name}', where {name} is a __set_name__ parameter. self.name is an attribute of the object of the Integer class. This object is used in the {owner} class
        self.name = "_" + name

    def __get__(self, instance, owner):     #gets the 'self.name' attribute to the object 'self' of class 'Integer', which is used in the object 'instance' of the class 'owner'
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
# class StringValue:
#     def __init__(self, validator):
#         self.validator = validator
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, obj, owner):
#         return getattr(obj, self.name)
#
#     def __set__(self, obj, value):
#         if self.validator.validate(value): return setattr(obj, self.name, value)
#         return None
#
#
# class ValidateString:
#     def __init__(self, min_length: int = 3, max_length: int = 100):
#         self.min_length = min_length
#         self.max_length = max_length
#
#     def validate(self, string):
#         return isinstance(string, str) and self.min_length <= len(string) <= self.max_length
#
#
# class RegisterForm:
#
#     login = StringValue(ValidateString())
#     password = StringValue(ValidateString())
#     email = StringValue(ValidateString())
#
#     def __init__(self, login, password, email):
#         self.login = login
#         self.password = password
#         self.email = email
#
#     def get_fields(self):
#         return [self.login, self.password, self.email]
#
#     def show(self):
#         print(f'<form>\nЛогин: {self.login}\nПароль: {self.password}\n<Email>: {self.email}\n</form>')


# min_length, max_length = 5, 100
# st = StringValue(validator=ValidateString(min_length, max_length))


'''task3'''
class StringValue:
    def __init__(self, min_length: int = 2, max_length: int = 50):
        self.min_length = min_length
        self.max_length = max_length

    def __length_is_correct(self, string):
        return isinstance(string, str) and self.min_length <= len(string) <= self.max_length

    def __set_name__(self, obj, name):
        self.name = "_" + name

    def __get__(self, obj, owner):
        return getattr(obj, self.name)

    def __set__(self, obj, value):
        if self.__length_is_correct(value):
            return setattr(obj, self.name, value)
        return None


class PriceValue:
    def __init__(self, max_price: float | int = 10000) -> None:
        self.max_price = max_price

    def __price_is_correct(self, price):
        return type(price) in (int, float) and price <= self.max_price

    def __set_name__(self, obj, name):
        self.name = "_" + name

    def __get__(self, obj, owner):
        return getattr(obj, self.name)

    def __set__(self, obj, value):
        if self.__price_is_correct(value): return setattr(obj, self.name, value)
        return None


class Product:

    name = StringValue()
    price = PriceValue()

    def __init__(self, name: StringValue, price: PriceValue):
        self.name = name
        self.price = price


class SuperShop:
    def __init__(self, name: str):
        self.name = name
        self.goods = []

    def add_product(self, product: Product) -> None:
        self.goods.append(product)

    def remove_product(self, product: Product) -> None:
        self.goods.remove(product)


'''task4'''
class Thing:
    def __init__(self, name: str, weight: float | int) -> None:
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.__things = []

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing: Thing) -> None:
        if thing.weight + sum(thing.weight for thing in self.__things) <= self.max_weight:
            self.__things.append(thing)

    def remove_thing(self, indx: int) -> None:
        self.__things.pop(indx)

    def get_total_weight(self):
        return sum(elem.weight for elem in self.__things)


'''task5'''
class Telecast:
    def __init__(self, id, name, duration):
        self.__id = id
        self.__name = name
        self.__duration = duration

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, value):
        self.__name = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        self.__duration = value


class TVProgram:
    def __init__(self, channel_name: str) -> None:
        self.channel_name = channel_name
        self.items = []

    def add_telecast(self, tl):
        self.items.append(tl)

    def remove_telecast(self, indx: int) -> None:
        for elem in self.items:
            if indx == elem.uid:
                self.items.remove(elem)

