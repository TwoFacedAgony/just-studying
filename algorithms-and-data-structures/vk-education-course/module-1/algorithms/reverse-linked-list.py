class ComponentLL:
    def __init__(self, value, tail=None):
        self.value = value
        self.tail = tail


class LinkedList:
    def __init__(self):
        self.__components = []

    def add(self, component):
        self.__components.append(component)
        if len(self.__components) != 1:
            self.__components[-2].tail = component

    def remove(self, index):
        self.__components[index].tail = None
        self.__components.pop(index)
        if index != 0 and len(self.__components) :
        self.__components[index - 1].head = None
