

from pathfinding.recursive_backtracking.recursive_backtracking import RecursiveBacktracking

class Hunt_and_Kill(RecursiveBacktracking):

    def __init__(self):
        RecursiveBacktracking.__init__(self)
        self.unvisited = self.grid

    def perform(self):
        while True:
            self.counting += 1

            print(self.startNode)
            self.startNode.visited = True
            self.univisted[self.startNode.x].pop(self.startNode.y)
            neighbours = self.countNeighbours(self.startNode.x, self.startNode.y)

            if len(neighbours) != 0:
                nextNode = self.chooseNextNode(neighbours)
                self.updateVertices(nextNode)
                self.startNode = nextNode


            elif len(self.unvisited) == 0:
                self.startNode = self.unvisited.pop(0)