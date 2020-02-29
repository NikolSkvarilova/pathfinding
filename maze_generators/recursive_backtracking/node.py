

class Node:
    def __init__(self, visited=False, pos=(), name="George"):
        self.visited = visited
        self.pos = self.x, self.y = pos[0], pos[1]
        self.name = name

    def __repr__(self):
        return "{}".format(self.name)