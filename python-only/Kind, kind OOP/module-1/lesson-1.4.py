'''task1'''
from types import NoneType


class MediaPlayer:
    def open(self, file: str) -> None:
        self.filename = file

    def play(self) -> None:
        print(f"Воспроизведение {self.filename}")


media1 = MediaPlayer()
media2 = MediaPlayer()

media1.open("filemedia1")
media2.open("filemedia2")

media1.play()
media2.play()


'''task2'''
class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data: list) -> None:
        self.data = data

    def draw(self) -> None:
        [(print(elem, end=' ') if index != len(self.data) else print(elem)) if self.LIMIT_Y[0] <= elem <= self.LIMIT_Y[1] else None for index, elem in enumerate(self.data)]


graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()


'''task3'''
import sys


class StreamData:
    def create(self, fields: tuple, lst_values: list[str]) -> bool:
        if len(fields) == len(lst_values):
            # for index, value in enumerate(lst_values):
            #     exec(f"self.{fields[index]} = {value}")
            self.__dict__ = dict(zip(fields, lst_values))
            return True
        else:
            return False


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


# sr = StreamReader()
# data, result = sr.readlines()


'''task4'''
import sys

# программу не менять, только добавить два метода
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data: list[str]) -> None:
        for elem in data:
            self.lst_data.append(dict(zip(DataBase.FIELDS, elem.split(' '))))

    def select(self, a: int, b: int) -> list:
        b = len(self.lst_data) if b >= len(self.lst_data) else b
        return self.lst_data[a:b+1]

# db = DataBase()
# db.insert(lst_in)


'''task5'''
class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}

        self.tr.setdefault(eng, [])
        if eng in self.tr['tr'].keys():
            self.tr['tr'][eng] = rus

    def remove(self, eng):
        del self.tr['tr'][eng]

    def translate(self, eng):
        return self.tr['tr'][eng]


tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
print(tr.remove("car"))
print(tr.__dict__)
print(tr.translate("go"))