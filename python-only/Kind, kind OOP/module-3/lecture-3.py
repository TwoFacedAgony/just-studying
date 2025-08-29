class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left

    def __getattribute__(self, item):
        print('__getattribute__')
        if item == 'x':
            raise ValueError("Access denied")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, item, value):
        print('__setattr__')
        if item == 'z':
            raise AttributeError("Cannot create z attribute")
        else:
            object.__setattr__(self, item, value)

    def __getattr__(self, item):
        print('__getattr__')

    def __delattr__(self, item):
        print(f'__delattr__: {item}')
        object.__delattr__(self, item)


pt1 = Point(0, 2)
pt1.set_bound(1)
print('\n')

try:
    x1 = pt1.x
    print('x1 is set\n\n')
except ValueError:
    y1 = pt1.y
    print('y1 is set\n\n')

try:
    pt1.z = 4
    print('pt1.z is set\n\n')
except AttributeError:
    print('pt1.z is undefined\n\n')

pt1.a
pt1.MAX_COORD
pt1.MIN_COORD

print('\n')
del pt1.x, pt1.y
print(pt1.__class__, Point)