from ssl import _PasswordType
from CreateMaze import *
from Stack import *
import random
#maze = CreateBlankMaze(10)
maze = ["000000000",
        "000000000",
        "000000000",
        "000000000",
        "000000000",
        "000000000",
        "000000000",
        "000000000",
        "000000000"]

pprint(maze)


def is_connected(maze,pos):
    connected = False
    try:
        if maze[pos[1]+1][pos[0]] == "1":  ## check down
            connected = True
    except:
        pass
    try:
        if maze[pos[1]-1][pos[0]] == "1": ## check up
            connected = True
    except:
        pass
    try:
        if maze[pos[1]][pos[0]+1] == "1": ## check right
            connected = True
    except:
        pass
    try:
        if maze[pos[1]][pos[0]-1] == "1":  ## check left
            connected = True
    except:
        pass
    return connected




def select_start(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if is_connected(maze,[j,i]) == False and maze[j][i] == "0":  ## checks node isn't connected to maze and is open 
                return [i,j]  ## returns coords as [y,x] because thats how navigating the array works
    return "END"   ## returns when no start nodes left

print(select_start(maze))

def findpath(maze,start):
    directions = ["up","down","left","right"] ## used to make code make more sense
    path = Stack()  ## stack for path
    path.push(start) ## add start to stack
    while is_connected(maze,start) != True: ## while path is not connected
        direction = random.choice(directions)
        if direction == "up":
            pass
        elif direction == "down":
            pass
        elif direction == "left":
            pass
        elif direction == "right":
            pass
    return path ## return path when connected
        
    

## select start and check not completed
## findpath
## add path to maze
"""
def WilsonsMaze(size):
    maze = CreateBlankMaze(size) ## make blank maze square
    while select_start(maze) != "END":  ## ends when maze is complete
        pos = select_start(maze) ## select start positon
"""
