

from recursive_backtracking import RecursiveBacktracking as rb

if __name__ == "__main__":
    maze = rb(cols=10, rows=20)                                    
    maze.perform()
    print(f"Total number of rounds: {maze.counting}.")
