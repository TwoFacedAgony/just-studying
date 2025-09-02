# FIFO: First in -> First out
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        if self.head is None:
            self.head