from stack import *

maze = ["10000010",
        "10111010",
        "10001010",
        "11111110",
        "10010010",
        "11111010",
        "10000010",
        "11002110"]


# Define the start and end points
start = (0, 0)
end = (4, 7)

# Define the directions for moving in the maze (right, down, left, up)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(maze, start, end):
    stack = Stack(1000)
    stack.push(start)
    visited = set()
    path = []

    while stack.isEmpty() == False:
        current = stack.spop()
        if current in visited:
            continue
        visited.add(current)
        path.append(current)

        if current == end:
            return path

        for direction in directions:
            next_cell = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= next_cell[0] < maze.shape[0] and 0 <= next_cell[1] < maze.shape[1] and maze[next_cell] == 1:
                stack.append(next_cell)

    return None

# Solve the maze
solution = dfs(maze, start, end)
if solution:
    print("Path found:", solution)
else:
    print("No path found")
    
    