# Recursive Backtracking algorithm
The depth-first **search algorithm** of **maze generation** is frequently implemented using *backtracking*. This can be described with a following recursive routine:

    (1) Given a current cell as a parameter,
    (2) Mark the current cell as visited
    (3) While the current cell has any unvisited neighbour cells
        (1) Chose one of the unvisited neighbours
        (2) Remove the wall between the current cell and the chosen cell
        (3) Invoke the routine recursively for a chosen cell

which is invoked once for any initial cell in the area.

A disadvantage of this approach is a **large depth of recursion** – in the worst case, the routine may need to recur on every cell of the area being processed, which may exceed the maximum recursion stack depth in many environments. As a solution, the same bactracking method can be implemented with **an explicit stack**, which is usually allowed to grow much bigger with no harm.

    (1) Choose the initial cell, mark it as visited and push it to the stack
    (2) While the stack is not empty
        (1) Pop a cell from the stack and make it a current cell
        (2) If the current cell has any neighbours which have not been visited
            (1) Push the current cell to the stack
            (2) Choose one of the unvisited neighbours
            (3) Remove the wall between the current cell and the chosen cell
            (4) Mark the chosen cell as visited and push it to the stack

> source: https://en.wikipedia.org/wiki/Maze_generation_algorithm

***

## How my code works?
First, let's look at the `main.py` file. We need to import our main class implementing the Recursice Backtracking algorithm. 

The
```python
if __name__ == "__main__": 
    pass 
```
means that you run the `main.py` ***directly***. For example: if you import `main.py` to another file - foo.py (using `import`) and run the foo.py file, the code in this condition won't be executed. But if you run the main.py file (using python3 main.py for example), the code will be executed.

Next, let's take a look at 
```python
    maze = rb(cols=10, rows=10)
```
This simply means that you have created an object of `RecursiveBacktracking` class (which is imported under the name 'rb'). The `cols=10` and `rows=10` says that the maze (it is always a square or a rectangle) is going to have 10 columns and 10 rows, so it creates a grid 10x10.

Last simple command which we have to write to implement our algorithm:
```python
maze.perform()
```
This performs the Recursive Backtracking algorithm and returns list of vertices. Vertice is something like a line between two points in the grid. When we move from one node to another in the algorithm, it creates the instance of `Vertice` class with `pointing` property in the form pointing=(fromNode, toNode). So basically a tuple with two nodes in it. I have done this because I want to visualize the process of creating the maze and the vertices will serve as "'you can go from `froomNode` to `toNode`' (path); if there is not a vertice between two nodes, it will be visualized like a wall. 

The
```python
print(f"Total number of rounds: {maze.counting}.")
```
just prints the total number of rounds that the algortihm has to perform until it has visited all of the nodes. The number is equal to
```
2*(cols*row) - 2 
```