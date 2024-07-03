import random

def CreateBlankMaze(size):
    maze = []
    for i in range(size):
        maze.append("0"*size)
    return maze


def pprint(maze):
    for i in range(len(maze)):
        print(maze[i])


def add_end(maze):
    size = len(maze)-1
    end_range = len(maze)//5 ## change how close to bottom right end is
    found = False
    while found == False:
        end_y = size - (random.randint(0,end_range))
        end_x = size - (random.randint(0,end_range))
        if maze[end_y][end_x] == "1": ## checks goal would be in maze
            found = True
            row = list(maze[end_y])  
            row[end_x] = "2"
            row = "".join(row)
            maze[end_y] = row ## adds goal to maze
            return maze

