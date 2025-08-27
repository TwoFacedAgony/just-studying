'''task1'''
from types import new_class


class AbstractClass:
    def __new__(cls, *args, **kwargs):
        return "Ошибка: нельзя создавать объекты абстрактного класса"


'''task2'''
class SingletonFive:
    __instance = None
    __classes_count = 0
    def __new__(cls, *args, **kwargs):
        if cls.__classes_count < 5:
            cls.__classes_count += 1
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name: str) -> None:
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]
print(objs[0].name)


'''task3'''
TYPE_OS = 1


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    def __new__(cls, *args, **kwargs):
        obj = DialogWindows() if TYPE_OS == 1 else DialogLinux()
        setattr(obj, 'name', args[0])
        return obj


dlg = Dialog("name")
print(isinstance(dlg, Dialog))


'''task4'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        return type(self)(self.x, self.y)


'''task5'''
class Factory:
    def build_sequence(self):
        return []

    def build_number(self, string):
        return int(string)


class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


ld = Loader()
s = input()
res = ld.parse_format(s, Factory())