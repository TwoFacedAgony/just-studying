from re import Match


class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg): #works from the class. it has the access to the class attrs, NOT local attrs
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y): #works from the class objects. it has the access to the local attributes and class attrs
        self.x = self.y = 0
        if Vector.validate(x) and Vector.validate(y):
            self.x = x
            self.y = y

    def get_coord(self): #works from the class objects. it has the access to the local attributes and class attrs
        return self.x, self.y

    @staticmethod
    def norm2(x, y): #works from the class objects. it has the access only to the function attrs
        #do not write Vector.MAX_COORD cuz if the name of the class changes, it is important to edit the in-method name
        return x ** 2 + y ** 2


# v = Vector(1, 2)
# print(Vector.validate(5))
# res = Vector.get_coord(v)
# print(res)
# print(Vector.norm2(5, 6))
#
# v2 = Vector(2, 300)
# print(Vector.validate(200))
# res = Vector.get_coord(v2)
# print(res)


'''task1'''
class Factory:
    @staticmethod
    def build_sequence():
        return []

    @staticmethod
    def build_number(string: str) -> float:
        return float(string)

class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


'''task2'''
from string import ascii_lowercase, digits


class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name: str, size: int=10) -> None:
        self.name = name
        self.size = size
        self.check_name(name)

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name: str) -> bool:
        if 3 <= len(name) <= 50 and all([i in cls.CHARS_CORRECT for i in name]):
            return True
        else:
            raise ValueError("некорректное поле name")


class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name: str, size: int = 10) -> None:
        self.name = name
        self.size = size
        self.check_name(name)

    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name: str) -> bool:
        if 3 <= len(name) <= 50 and all([i in cls.CHARS_CORRECT for i in name]):
            return True
        else:
            raise ValueError("некорректное поле name")


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
# html = login.render_template()
# log = TextInput("ЛОГИН")
# print(log.get_html())


'''task3'''
import re


class CardCheck:
    @staticmethod
    def check_card_number(number: str) -> bool:
        return bool(re.match(r"^([\d]{4}-){3}[\d]{4}$", number))

    @staticmethod
    def check_name(name: str) -> bool:
        return bool(re.match(r'^[A-Z\d]+ [A-Z\d]+$', name))


print(bool(re.match(r"^([\d]{4}-){3}[\d]{4}$", '2342-3423-23d23-2322')))


'''task4'''
class Video:
    def create(self, name: str) -> None:
        self.name = name

    def play(self):
        print(f'воспроизведение видео {self.name}')


class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx: int):
        cls.videos[video_indx].play()


v1, v2 = Video(), Video()

v1.create("Python")

v2.create("Python ООП")

YouTube.add_video(v1)
YouTube.add_video(v2)

YouTube.play(0)
YouTube.play(1)


'''task5'''
class Application:
    def __init__(self, name: str, blocked: bool = False) -> None:
        self.name = name
        self.blocked = blocked


class AppStore:
    def __init__(self) -> None:
        self.store = []

    def add_application(self, app) -> None:
        self.store.append(app)

    def remove_application(self, app) -> None:
        self.store.remove(app)

    def block_application(self, app: Application) -> None:
        for elem in self.store:
            if elem == app:
                elem.blocked = True
                break

    def total_apps(self) -> int:
        return len(self.store)


'''task6'''
class Message:
    def __init__(self, text: str, fl_like: bool = False) -> None:
        self.text = text
        self.fl_like = fl_like


class Viber:
    msgs = {}

    @classmethod
    def add_message(cls, msg: Message) -> None:
        cls.msgs[id(msg)] = msg

    @classmethod
    def remove_message(cls, msg: Message) -> None:
        cls.msgs.pop(id(msg))

    @classmethod
    def set_like(cls, msg: Message) -> None:
        msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_message(cls, num: int) -> None:
        print(cls.msgs[-num:])

    @classmethod
    def total_messages(cls) -> int:
        return len(cls.msgs)

    # @classmethod
    # def print_messages(cls) -> None:
    #     print(cls.msgs.keys())
    #     for msg in cls.msgs.values():
    #         print(msg)

msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("<UNK> <UNK> <UNK> Python <UNK>."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
# Viber.print_messages()
Viber.remove_message(msg)