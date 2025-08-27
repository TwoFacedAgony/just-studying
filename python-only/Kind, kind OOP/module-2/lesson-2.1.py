'''ENCAPSULATION'''


class Point:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y


# pt = Point(1, 2)
# pt.x = 100
# pt.y = "coord_y"
# print(pt.x, pt.y)


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


