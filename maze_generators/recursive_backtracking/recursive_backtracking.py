
import random
from node import Node
from vertice import Vertice

class RecursiveBacktracking:

    def __init__(self, cols=3, rows=3, startNodePos=(0, 0)):
        self.cols = cols
        self.rows = rows
        self.grid = self.make2DArray()

        # history of visited nodes
        self.stack, self.vertices = [], []
        
        self.startNode = self.grid[startNodePos[0]][startNodePos[1]]
        # total number of steps (1 step = moving from one node to another)
        self.counting = 0

    def make2DArray(self):
        # list of numbers just for setting names as numbers
        names = list(range(self.cols*self.rows))
        return [[Node(pos=(x, y), name=names.pop(0)) 
                for y in range(self.cols)] 
                for x in range(self.rows)]

    def countNeighbours(self, x, y):
        neighbours = []

        if x - 1 >= 0:
            if self.grid[x-1][y].visited == False:
                neighbours.append(self.grid[x-1][y])

        if x + 1 <= len(self.grid)-1:
            if self.grid[x+1][y].visited == False:
                neighbours.append(self.grid[x+1][y])

        if y - 1 >= 0:
            if self.grid[x][y-1].visited == False:
                neighbours.append(self.grid[x][y-1])

        if y + 1 <= len(self.grid[0])-1:
            if self.grid[x][y+1].visited == False:
                neighbours.append(self.grid[x][y+1])

        return neighbours

    def chooseNextNode(self, arr):
        return random.choice(arr)

    def updateVertices(self, to):
        self.vertices.append(Vertice(pointing=(self.startNode, to)))

    def addToStack(self, *args):
        if len(args) == 0:
            self.stack.append(self.startNode)
        else:
            for node in args:
                self.stack.append(node)

    def perform(self):
        while True:
            self.counting += 1
        
            print(self.startNode)
            self.startNode.visited = True
            neighbours = self.countNeighbours(self.startNode.x, self.startNode.y)
            
            if len(neighbours) != 0:
                nextNode = self.chooseNextNode(neighbours)
                self.updateVertices(nextNode)
                self.startNode = nextNode
                self.addToStack()

            elif len(self.stack) != 1:
                self.startNode = self.stack.pop()

            else:
                return self.vertices