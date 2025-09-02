# LIFO: Last in -> First out
class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        if self.top is None:
            self.top = item

        else:
            item.next = self.top
            self.top = item

    def pop(self):
        if not self.top is None:
            popped = self.top
            self.top = self.top.next
            self.top.next = None
            return popped
        return None