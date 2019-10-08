from node import *
import json
from queue import PriorityQueue, Queue


class Graph:
    def __init__(self):
        self.nodes = json.load(open("villes.json"), object_hook=lambda n: Node(n["name"], n["x"], n["y"]))
        # while len(self.nodes) < size:
        #     self.nodes.add(Node(randint(0, size * 2), randint(0, size * 2)))
        # assert len(self.nodes) == size
        self.closed = Queue()
        self.open = PriorityQueue()
        for n in self.nodes:
            self.open.put(n)

    def shortest_path(self, start):
        self.open.put(start)
        while not self.open.empty():
            node = self.open.get()
            for n in self.nodes:
                if not n in self.closed:
                    if n in self.open:
                        x = self.open.
