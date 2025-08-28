'''learning property'''
class Person:
    def __init__(self, name: str, old: int):
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old

    def set_old(self, old: int):
        self.__old = old

    old = property(get_old, set_old) #its priority is higher than the local attributes' priority

p = Person('john', 20)

# p.set_old(21)
# print(p.get_old())

print(p.old)
p.old = 21
print(p.old)
print(p.__dict__)