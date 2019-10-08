class Node:
    def __init__(self, name, x, y, cost=0, heuristic=0):
        self.name = name
        self.x = x
        self.y = y
        self.cost = cost
        self.heuristic = heuristic

    def __str__(self):
        return f"({self.x},{self.y})"

    def __eq__(self, other):
        if type(other) != type(self) or self.x != other.x or self.y != other.y:
            return False
        return True

    def __hash__(self):
        return hash(('x', self.x, 'y', self.y))

    def __cmp__(self, other):
        if self.heuristic < other.heuristic:
            return 1
        elif self.heuristic == other.heuristic:
            return 0
        return -1
