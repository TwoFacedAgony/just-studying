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