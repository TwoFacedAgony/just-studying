'''task1'''
from random import randint, choice


class RandomPassword:
    def __init__(self,
               psw_chars: str="qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*",
               min_length: int = 5,
               max_length: int = 20):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self):
        return "".join(choice(self.psw_chars) for _ in range(randint(self.min_length, self.max_length)))


rnd = RandomPassword()
lst_pass = [rnd() for _ in range(3)]


'''task2'''
class ImageFileAcceptor:
    def __init__(self, extensions: tuple) -> None:
        self.extensions = extensions

    def __call__(self, filename: str):
        if filename[filename.rfind('.') + 1:] in self.extensions:
            return filename


'''task3'''
class LengthValidator:
    def __init__(self, min_length: int, max_length: int):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, string: str):
        return self.min_length <= len(string) <= self.max_length


class CharsValidator:
    def __init__(self, chars: str):
        self.chars = chars

    def __call__(self, string: str):
        return all((symbol in self.chars) for symbol in string)


'''task4'''
class DigitRetrieve:
    def __call__(self, string: str):
        if (string.isdigit() or string[1:].isdigit()) and '.' not in string:
            return int(string)
        return None


'''task5'''
class RenderList:
    def __init__(self, type_list: str) -> None:
        self.type_list = type_list
        if self.type_list != 'ol':
            self.type_list = 'ul'

    def __call__(self, menu: list[str]) -> str:
        result = f"<{self.type_list}>\n"
        for position in menu:
            result += f"<li>{position}</li>\n"
        result += f"</{self.type_list}>"
        return result


'''task6'''
class HandlerGET:
    def __init__(self, function):
        self.function = function

    def get(self, func: callable, request: dict, *args, **kwargs) -> str:
        if 'method' in request.keys():
            return f"{request['method']}: {func(args)}" if request['method'] == 'GET' else None
        return f"GET: {func(args)}"

    def __call__(self, request: dict):
        return self.get(self.function, request)


'''task7 - unfinished'''
class Handler:
    def __init__(self, methods: tuple = ("GET",)) -> None:
        self.methods = methods

    def get(self, func: callable, request: dict, *args) -> str:
        if 'method' in request.keys() and request['method'] == 'GET':
            return f"GET: {func(args)}"

    def post(self, func: callable, request: dict, *args) -> str:
        if 'method' in request.keys() and request['method'] == 'POST':
            return f"POST: {func(args)}"

    def __call__(self, func):
        def wrapper(request: dict, *args, **kwargs):
            if 'method' in request.keys():
                match request['method']:
                    case 'GET':
                        return self.get(func, request, *args)
                    case 'POST':
                        return self.post(func, request, *args)
        return wrapper


'''task8'''
class InputDigits:
    def __init__(self, function: callable) -> None:
        self.function = function

    def __call__(self):
        return list(map(int, self.function().split(' ')))

@InputDigits
def input_dg():
    return input()


'''task9'''