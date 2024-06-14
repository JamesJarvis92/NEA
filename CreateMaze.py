def CreateBlankMaze(size):
    maze = []
    for i in range(size):
        maze.append("0"*size)
    return maze


def pprint(maze):
    for i in range(len(maze)):
        print(maze[i])

