class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.array = self.__make_array(self.capacity)
        self.count = 1

    def append(self, element):
        if self.size == self.capacity:
            print(f'resizing {self.capacity} to {self.capacity * 2}')
            self.__resize_to_bigger()

        self.array[self.size-1] = element
        self.size += 1

    def remove(self, index):
        if self.size <= self.capacity // 4:
            print(f'resizing {self.capacity} to {self.capacity // 2}')
            self.__resize_to_smaller()

        self.array.pop(index)
        self.size -= 1

    def __resize_to_bigger(self):
        new_capacity = self.capacity * 2
        new_array = self.__make_array(new_capacity)

        for i in range(self.size):
            new_array[i] = self.array[i]

        self.capacity = new_capacity
        self.array = new_array

    def __resize_to_smaller(self):
        new_capacity = self.capacity // 2
        new_array = self.__make_array(new_capacity)

        for i in range(self.size):
            new_array[i] = self.array[i]

        self.capacity = new_capacity
        self.array = new_array

    @staticmethod
    def __make_array(capacity):
        return [None for _ in range(capacity)]

# array = DynamicArray()
# for elem in [1 for _ in range(15)]:
#     array.append(elem)
#
# for elem in [1 for _ in range(15)]:
#     array.remove(elem)