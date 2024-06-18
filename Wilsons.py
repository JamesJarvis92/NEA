
from CreateMaze import *
from stack import *
import random

#maze = CreateBlankMaze(10)
maze = ["000001000",
        "000001000",
        "000001000",
        "000001000",
        "000001000",
        "111111000",
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

def in_maze(maze,pos):
    try:
        x = maze[pos[1]][pos[0]]
        if pos[1]>=0 and pos[0]>=0:
            return True
        else:
            return False
    except:
        return False
print(in_maze(maze,[1,1]))

def remove_loop(stack,pos): 
    while stack.isempty() == False: ## while values in stack
        top = stack.spop()
        if top == pos: ## if finds pos in stack while removing returns stack without loop
            stack.push(pos)
            return stack

def findpath(maze,start):
    directions = ["up","down","left","right"] ## used to make code make more sense
    path = Stack(len(maze)*(len(maze[0])))  ## stack for path
    path.push(start) ## add start to stack
    while is_connected(maze,path.peek()) != True: ## while path is not connected
        pos = path.peek()
        direction = random.choice(directions)
        move_is_valid = True
        if direction == "up":
            new_pos = [pos[0]+1,pos[1]]
        elif direction == "down":
            new_pos = [pos[0]-1,pos[1]]
        elif direction == "left":
            new_pos = [pos[0],pos[1]-1]
        elif direction == "right":
            new_pos = [pos[0],pos[1]+1]
        if in_maze(maze,new_pos):    ## need to check there isnt a loop
            pass
            path.push(new_pos)
            
    return path.seestack() ## return path when connected
        
    
print(findpath(maze,[0,0]))
## add random cell that isn't [0,0] so path has a goal
## select start and check not completed
## findpath
## add path to maze
"""
def WilsonsMaze(size):
    maze = CreateBlankMaze(size) ## make blank maze square
    while select_start(maze) != "END":  ## ends when maze is complete
        pos = select_start(maze) ## select start positon
"""
