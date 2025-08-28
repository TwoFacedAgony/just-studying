'''task 1'''
class Money:
    def __init__(self, money):
        self.money = money

    def __del__(self):
        pass


'''task 2'''
class Point:
    def __init__(self, x: int, y: int, color: str = 'black'):
        self.x = x
        self.y = y
        self.color = color


# points = []
# [points.append(Point(i, i)) if not i == 3 else points.append(Point(i, i, 'yellow')) for i in range(1, 1 + 1000 * 2, 2)]
# print(len(points))


'''task 3'''
import random


class Line:
    def __init__(self, a: int, b: int, c: int, d: int):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a: int, b: int, c: int, d: int):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a: int, b: int, c: int, d: int):
        self.sp = (a, b)
        self.ep = (c, d)

all_figure_classes = ['Line', 'Rect', 'Ellipse']
elements = []
for i in range(217):
    current_figure = random.choice(all_figure_classes)
    if current_figure == 'Line':
        elements.append(Line(0, 0, 0, 0))
    elif current_figure == 'Rect':
        elements.append(Rect(random, random, random, random))
    else:
        elements.append(Ellipse(random, random, random, random))


'''task 4'''
class TriangleChecker:
    def __init__(self, a: int, b: int, c: int) -> None:
        self.sides = [a, b, c]

    def is_triangle(self) -> int:
        for side in self.sides:
            if not (isinstance(side, float) or isinstance(side, int)) or side <= 0 or side is True:
                return 1
            elif side >= sum(self.sides) / 2:
                return 2
        return 3


# a, b, c = map(int, input().split())
# tr = TriangleChecker(a, b, c)
# print(tr.is_triangle())


'''task 5'''
class Graph:
    def __init__(self, data: list[int], is_show: bool = True) -> None:
        self.data = data.copy()
        self.is_show = is_show

    def set_data(self, data: list[int]) -> None:
        self.data = data

    def show_table(self):
        print(*self.data) if self.is_show else print('Отображение данных закрыто')

    def show_graph(self):
        print(f"Графическое отображение данных: {' '.join(map(str, self.data))}") if self.is_show else print('Отображение данных закрыто')

    def show_bar(self):
        print(f"Столбчатая диаграмма: {' '.join(map(str, self.data))}") if self.is_show else print('Отображение данных закрыто')

    def set_show(self, fl_show: bool) -> None:
        self.is_show = fl_show


# data_graph = list(map(int, input().split()))
# gr = Graph(data_graph)
# gr.show_bar()
# gr.set_show(fl_show=False)
# gr.show_table()


'''task 6'''
class CPU:
    def __init__(self, name: str, fr: int) -> None:
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name: str, volume: int) -> None:
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name: str, cpu: CPU, total_mem_slots: int, mem_slots: list[Memory]) -> None:
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = total_mem_slots
        self.mem_slots = mem_slots

    def get_config(self) -> list[str]:
        return [f'Материнская плата: {self.name}',
                f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}',
                f'Память: {' '.join((f'{slot.name} - {slot.volume};' for slot in self.mem_slots))}'[:-1]]


mb = MotherBoard('MSI', CPU('Ryzen R7500f', 1), 2, [Memory('XPG', 6000) for i in range(2)])
print(mb.get_config())


'''task 7'''
class Cart:
    def __init__(self, goods: list=[]):
        self.goods = goods

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f'{product.name}: {product.price}' for product in self.goods]


class Table:
    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price


class TV:
    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price


cart = Cart()
cart.add(TV('samsung', 2))
cart.add(TV('lg', 4))
cart.add(Table('wooden', 2))
cart.add(Notebook('samsung', 2))
cart.add(Notebook('dell', 1))
cart.add(Cup('the best boss', 1000))
print(cart.get_list())


'''task 8 - idk works in pycharm'''
import sys


class ListObject:
    def __init__(self, data: str) -> None:
        self.next_obj = None
        self.data = data

    def link(self, obj) -> None:
        self.next_obj = obj


# lst_in = ['1. Первые шаги в ООП',
#           '1.1 Как правильно проходить этот курс',
#           '1.2 Концепция ООП простыми словами',
#           '1.3 Классы и объекты. Атрибуты классов и объектов',
#           '1.4 Методы классов. Параметр self',
#           '1.5 Инициализатор init и финализатор del',
#           '1.6 Магический метод new. Пример паттерна Singleton',
#           '1.7 Методы класса (classmethod) и статические методы (staticmethod)']
# lst_in = list(map(str.strip, sys.stdin.readlines())) # список lst_in в программе не менять
#
# task_list = []
#
# for index, elem in enumerate(lst_in):
#     task_list.append(ListObject(elem))
#
# head_obj = ListObject('')
# head_obj.link(task_list[0].data)
# # print(head_obj.next_obj)
#
# for next_elem_index, elem in enumerate(task_list, start=1):
#     if next_elem_index != len(task_list):
#         elem.link(task_list[next_elem_index].data)
#
# [print(f'{elem.data}, {elem.next_obj}') for elem in task_list]
# print(task_list)

'''task 9 - unfinished'''
from random import shuffle


class Cell:
    def __init__(self, around_mines: int, mine: bool) -> None:
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, N: int, M: int) -> None:
        self.N = N
        self.M = M
        self.pole = [[Cell() for _ in range(N)] for _ in range(N)]

    def init(self) -> None:
        mines_coords = [num for num in range(self.N ** 2)]
        shuffle(mines_coords)
        mines_coords = mines_coords[:self.M]
        for line_index, line in enumerate(self.pole):
            for col_index, col in enumerate(line):
                if col_index + line_index * self.N in mines_coords:
                    self.pole[line_index][col_index] = '*'
        print(self.pole)

    def show(self) -> None:
        for line in self.pole:
            print(*line)


