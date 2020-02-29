# Hunt and Kill algorithm
The **Hunt and Kill** algorithm is very similar to **Recursive Backtracker**. The only difference is how it handles ***dead ends***. As this algorithm doesn't use recursion, it can avoid the potential stack overflows that plague the Recursive Backtracker for large mazes.

The algorithm picks a **random location** and starts a **random walk**. It continues to walk until it hits a **dead end**. At this point, the Recursive Backtracker would take a step back, but the Hunt and Kill Algorithm does something different. Instead of backtracking, *it will scan the maze for an uncut cell at restart the walk process at that location. It continues this process until all cells have been cut.*

## Pseudo Code
```
(1) Select a random cell. This is the current cell. Add it 
    to the visited list.
(2) Randomly pick a cell adjacent to the current cell that 
    is not in the visited list. This becomes the current cell.
(3) Remove edge between the previous cell and the current 
    cell. Add the current cell to the visited list.
(4) Repeat 2 and 3 until travel is no longer possible.
(5) Scan the grid top --> bottom, left --> right.
    (a) If a non-visited cell is found:
        (1) The cell becomes the current cell.
        (2) Go to 2.
    (b) Else:
        - The algorithm is complete.
```


> source: Hunt and Kill Algorithm - Procedural Generation Algorithms. 301 Moved Permanently [online]. Available from: http://people.cs.ksu.edu/~ashley78/wiki.ashleycoleman.me/index.php/Hunt_and_Kill_Algorithm.html

In response, I refer to my [Recursive_Backtracking](https://github.com/NikolSkvarilova/code/tree/master/python/Recursive_Backtracking) project in this repo for more information.

