class Queue(list):
    def __init__(self):
        super().__init__(self)
        self.items = []

    def put(self, item):
        self.items.append(item)

    def get(self):
        return self.items.pop()


class PriorityQueue(Queue):
    def __init__(self):
        super().__init__()

    def put(self, item):
        super().put(item)
        self.items.sort()

    def get(self):
        x = super().get()
        self.items.sort()
        return x
