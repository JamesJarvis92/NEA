def CreateBlankMaze(size):
    maze = []
    for i in range(size):
        maze.append("0"*size)
    return maze

print(CreateBlankMaze(4))
