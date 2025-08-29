'''task1'''
class Book:
    def __init__(self, title: str = '', author: str = '', pages: int = 0, year: int = 0) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, name, value):
        match name:
            case 'title':
                if type(value) != str: raise TypeError("Неверный тип присваиваемых данных.")
            case 'author':
                if type(value) != str: raise TypeError("Неверный тип присваиваемых данных.")
            case 'pages':
                if type(value) != int: raise TypeError("Неверный тип присваиваемых данных.")
            case 'year':
                if type(value) != int: raise TypeError("Неверный тип присваиваемых данных.")

    # NOT MY REALIZATION, BTW LOOKS INTERESTING
    #
    # def __setattr__(self, key, value) -> None:
    #     if not isinstance(value, self.__annotations__.get(key, object)):
    #         raise TypeError("Неверный тип присваиваемых данных.")
    #     super().__setattr__(key, value)
    #
    # IT REQUIRES:
    #
    # title: str
    # author: str
    # pages: int
    # year: int

        object.__setattr__(self, name, value)


# book = Book("Python ООП", "Сергей Балакирев", 123, 2022)

'''task2'''
class Product:
    __ID = 0
    def __new__(cls, *args, **kwargs):
        cls.__ID = cls.__ID + 1
        newobj = super().__new__(cls)
        newobj.__setattr__('id', cls.__ID)
        return newobj

    def __init__(self, name: str, weight: int | float, price: int | float) -> None:
        self.name = name
        self.weight = weight
        self.price = price


    def __setattr__(self, name, value):
        match name:
            case 'name':
                if type(value) != str:
                    raise TypeError("Неверный тип присваиваемых данных.")
            case 'price':
                if not type(value) in (int, float) or value <= 0:
                    raise TypeError("Неверный тип присваиваемых данных.")
            case 'weight':
                if not type(value) in (int, float) or value <= 0:
                    raise TypeError("Неверный тип присваиваемых данных.")
            case 'id':
                if type(value) != int or value <= 0:
                    raise TypeError("Неверный тип присваиваемых данных.")

        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        if name == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")


class Shop:
    def __init__(self, name: str) -> None:
        self.name = name
        self.goods = []

    def add_product(self, product: Product) -> None:
        self.goods.append(product)

    def remove_product(self, product: Product) -> None:
        self.goods.remove(product)


'''task3'''
class LessonItem:
    def __init__(self, title: str, practices: int, duration: int) -> None:
        self.title = title
        self.practices = practices
        self.duration = duration

    def __getattr__(self, name):
        return False

    def __setattr__(self, name, value):
        match name:
            case 'title':
                if not isinstance(value, str):
                    raise TypeError("Неверный тип присваиваемых данных.")
            case 'practices':
                if not isinstance(value, int):
                    raise TypeError("Неверный тип присваиваемых данных.")
            case 'duration':
                if not isinstance(value, int):
                    raise TypeError("Неверный тип присваиваемых данных.")

        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        if not name in ['title', 'practices', 'duration']:
            object.__delattr__(self, name)


class Module:
    def __init__(self, name: str) -> None:
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson: LessonItem) -> None:
        self.lessons.append(lesson)

    def remove_lesson(self, indx: int) -> None:
        self.lessons.pop(indx)


class Course:
    def __init__(self, name: str) -> None:
        self.name = name
        self.modules = []

    def add_module(self, module: Module) -> None:
        self.modules.append(module)

    def remove_module(self, indx: int) -> None:
        self.modules.pop(indx)


def task3_tests():
    # TEST-TASK___________________________________
    course = Course("Python ООП")
    assert type(course.name) is str, "название курса должно быть строкой"
    assert type(course.modules) is list and len(
        course.modules) == 0, "modules должен быть списком, изначально список пуст"
    # add_module(self, module) - добавление нового модуля в конце списка modules;
    # remove_module(self, indx) - удаление модуля из списка modules по индексу в этом списке.
    assert hasattr(course, 'add_module'), "add_module необъявлен"
    assert hasattr(course, 'remove_module'), "remove_module необъявлен"

    #
    module_1 = Module("Часть первая")
    module_2 = Module("Часть вторая")
    assert type(module_1.name) is str, "название модуля должно быть строкой"
    assert type(module_1.lessons) is list and len(
        module_1.lessons) == 0, "lesson должен быть списком, изначально список пуст"
    # add_lesson(self, lesson) - добавление в модуль (в конец списка lessons) нового урока (объекта класса LessonItem);
    # remove_lesson(self, indx) - удаление урока по индексу в списке lessons.
    assert hasattr(module_1, "add_lesson"), "add_lesson необъявлен"
    assert hasattr(module_1, "remove_lesson"), "remove_lesson необъявлен"

    #
    les_1 = LessonItem("Урок 1", 7, 1000)
    les_2 = LessonItem("Урок 2", 10, 1200)
    assert type(les_1.title) is str, "название урока должно быть строкой"
    assert type(les_1.practices) is int and les_1.practices > 0, "practices должен быть целым числом больше ноля"
    assert type(les_1.duration) is int and les_1.practices > 0, "duration должен быть целым положительным числом"

    #
    # проверка методов
    course.add_module(module_1)
    course.add_module(module_2)
    assert len(course.modules) == 2 and course.modules[1] == module_2, "некоректно отработал метод add_module"
    course.remove_module(0)
    assert module_1 not in course.modules and len(course.modules) == 1, "некоректно отработал метод remove_module"
    #
    module_1.add_lesson(les_1)
    module_1.add_lesson(les_2)
    assert len(module_1.lessons) == 2 and module_1.lessons[1] == les_2, "некоректно отработал метод add_lesson"
    module_1.remove_lesson(0)
    assert les_1 not in module_1.lessons and len(module_1.lessons) == 1, "некоректно отработал метод remove_lesson"
    #
    # проверка методов - LessonItem
    # 1. Проверять тип присваиваемых данных локальным атрибутам. Если типы не соответствуют требованиям, то генерировать исключение командой:
    # raise TypeError("Неверный тип присваиваемых данных.")
    try:
        les_3 = LessonItem(3, 8, 900)
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалось исключение TypeError при записи некорректных данных в title"

    try:
        les_3 = LessonItem("Урок 2", 8.0, 900)
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалось исключение TypeError при записи некорректных данных в practices"

    try:
        les_3 = LessonItem("Урок 2", 8, 900, 0)
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалось исключение TypeError при записи некорректных данных в duration"

    # 2. При обращении к несуществующим атрибутам объектов класса LessonItem возвращать значение False.
    les_4 = LessonItem("Урок 2", 8, 900)
    assert hasattr(les_1, "__getattr__"), \
        "ошибка при обращении к несуществующему локальному атрибуту, метод должен вернуть False"
    assert les_4.value_not_atr is False, "ошибка при обращении к несуществующему локальному атрибуту, метод должен вернуть False"
    # 3. Запретить удаление атрибутов title, practices и duration в объектах класса LessonItem.
    assert hasattr(les_4, "__delattr__"), \
        "возможно вы не продумали запрет на удаление локальных атрибутов - title, practices и duration"
    try:
        del les_4.title
        del les_4.practices
        del les_4.duration
    except:
        ...
    else:
        if any(True if _ not in les_4.__dict__ else False for _ in ["title", "practices", "duration"]):
            print('Ошибка при удалении локальных атрибутов - title, practices и duration')

    print("Умница правильный ответ ))")


'''task4'''
class Picture:
    def __init__(self, name: str, artist: str, description: str):
        self.name = name
        self.artist = artist
        self.description = description


class Mummies:
    def __init__(self, name: str, area: str, description: str):
        self.name = name
        self.area = area
        self.description = description


class Papyri:
    def __init__(self, name: str, date: str, description: str):
        self.name = name
        self.date = date
        self.description = description

class Museum:
    def __init__(self, name: str):
        self.name = name
        self.exhibits = []

    def add_exhibit(self, obj: Picture|Mummies|Papyri):
        self.exhibits.append(obj)

    def remove_exhibit(self, obj: Picture|Mummies|Papyri):
        self.exhibits.remove(obj)

    def get_info_exhibit(self, indx: int) -> str:
        return f"Описание экспоната {self.exhibits[indx].name}: {self.exhibits[indx].description}"


'''task5'''
class AppVK:
    def __init__(self):
        self.name = "ВКонтакте"


class AppYouTube:
    def __init__(self, memory_max: int = 1024):
        self.memory_max = memory_max
        self.name = "YouTube"

class AppPhone:
    def __init__(self, numbers: dict) -> None:
        self.numbers = numbers
        self.phone_list = "словарь с контактами"
        self.name = "Phone"


class SmartPhone:
    def __init__(self, model: str) -> None:
        self.model = model
        self.apps = []

    def add_app(self, app: AppVK|AppYouTube|AppPhone) -> None:
        if all(app.__class__ != installed.__class__ for installed in self.apps): self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)


'''task6'''
class Circle:
    def __init__(self, x: float|int, y: float|int, radius: float|int) -> None:
        self.__x = x
        self.__y = y
        self.__radius = radius

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value

    def __setattr__(self, item, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            if item == 'radius':
                if value > 0: object.__setattr__(self, item, value)
            else:
                object.__setattr__(self, item, value)
        return False

    def __getattr__(self, item):
        return False

def tests_task_6():
    assert type(Circle.x) == property and type(Circle.y) == property and type(
        Circle.radius) == property, "в классе Circle должны быть объявлены объекты-свойства x, y и radius"

    try:
        cr = Circle(20, '7', 22)
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалось исключение TypeError при инициализации объекта с недопустимыми аргументами"

    cr = Circle(-20, -7, 1)
    cr = Circle(20, 7, 22)
    assert cr.x == 20 and cr.y == 7 and cr.radius == 22, "объекты-свойства x, y и radius вернули неверные значения"

    cr.radius = -10  # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
    assert cr.radius == 22, "при присваивании некорректного значения, прежнее значение изменилось"

    x, y = cr.x, cr.y
    assert x == 20 and y == 7, "объекты-свойства x, y вернули некорректные значения"
    assert cr.name == False, "при обращении к несуществующему атрибуту должно возвращаться значение False"

    try:
        cr.x = '20'
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалось исключение TypeError"

    cr.y = 7.8
    cr.radius = 10.6

# tests_task_6()


'''task7'''
class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 100

    def __init__(self, a: int|float, b: int|float, c: int|float) -> None:
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        self.__c = value

    def __setattr__(self, item, value):
        match item:
            case "MIN_DIMENSION":
                raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
            case "MAX_DIMENSION":
                raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
            case _:
                if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION: object.__setattr__(self, item, value)


'''task8'''
import time


class Mechanical:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, item, value):
        if item and isinstance(value, float) and value > 0:
            object.__setattr__(self, item, value)


class Aragon:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, item, value):
        if item and isinstance(value, float) and value > 0:
            object.__setattr__(self, item, value)


class Calcium:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, item, value):
        if item and isinstance(value, float) and value > 0:
            object.__setattr__(self, item, value)


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.__slots = dict((i, None) for i in range(1, 4))

    def add_filter(self, slot_num, filter_n):
        compatibility = {Mechanical: 1, Aragon: 2, Calcium: 3}
        if self.__slots[slot_num] is None:
            if compatibility[filter_n.__class__] == slot_num:
                self.__slots[slot_num] = filter_n

    def remove_filter(self, slot_num):
        self.__slots[slot_num] = None

    def get_filters(self):
        return (filter_n for filter_n in self.__slots.values())

    def water_on(self):
        return all(self.__slots.values()) and all(0 <= time.time() - filt.date <= self.MAX_DATE_FILTER for filt in self.__slots.values())


def tests_task_8():
    import time

    my_water = GeyserClassic()
    my_water.add_filter(1, Mechanical(time.time()))
    my_water.add_filter(2, Aragon(time.time()))

    assert my_water.water_on() == False, "метод water_on вернул True, хотя не все фильтры были установлены"

    my_water.add_filter(3, Calcium(time.time()))
    print(my_water.get_filters())
    assert my_water.water_on(), "метод water_on вернул False при всех трех установленных фильтрах"

    f1, f2, f3 = my_water.get_filters()
    assert isinstance(f1, Mechanical) and isinstance(f2, Aragon) and isinstance(f3,
                                                                                Calcium), "фильтры должны быть устанлены в порядке: Mechanical, Aragon, Calcium"

    my_water.remove_filter(1)
    assert my_water.water_on() == False, "метод water_on вернул True, хотя один из фильтров был удален"

    my_water.add_filter(1, Mechanical(time.time()))
    assert my_water.water_on(), "метод water_on вернул False, хотя все три фильтра установлены"

    f1, f2, f3 = my_water.get_filters()
    my_water.remove_filter(1)

    my_water.add_filter(1, Mechanical(time.time() - GeyserClassic.MAX_DATE_FILTER - 1))
    assert my_water.water_on() == False, "метод water_on вернул True, хотя у одного фильтра истек срок его работы"

    f1 = Mechanical(1.0)
    f2 = Aragon(2.0)
    f3 = Calcium(3.0)
    assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "неверное значение атрибута date в объектах фильтров"

    f1.date = 5.0
    f2.date = 5.0
    f3.date = 5.0

    assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "локальный атрибут date в объектах фильтров должен быть защищен от изменения"

tests_task_8()