
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


def is_connected_to_maze(maze,pos):
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
            if is_connected_to_maze(maze,[j,i]) == False and maze[j][i] == "0":  ## checks node isn't connected to maze and is open 
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


def surrounding_nodes(node):
    return [[node[0]+1,node[1]],[node[0]-1,node[1]],[node[0],node[1]+1],[node[0],node[1]-1]]

def remove_loop(stack):
    loop_lengths = [0]
    path = []
    new_pos = stack.spop() ## removes one wanting to be added
    pos2 = stack.spop()   ## removes one before to avoid false loop
    while stack.isEmpty() == False:
        path.append(stack.spop())
    path = path[::-1]
    for node in surrounding_nodes(new_pos):
        if node in path:
            x = path.index(node)
            loop_lengths.append(len(path)-x)   ## append lengths of loops
            

    for node in path:    ## makes testing work
        stack.push(node)
    stack.push(pos2)
    stack.push(new_pos)
    

    return max(loop_lengths)
    
        
    
        
def add_to_maze(path,maze): ## add path to maze
    for node in path:
        print(node[0],node[1])
        row = maze[node[0]]
        row = list(row)
        row[node[1]] = "1"
        row = "".join(row)
        maze[node[0]] = row
        #pprint(maze)
        print("\n")
    return maze

def findpath(maze,start):
    last_direction = "" ## so it can't go back in itself
    directions = ["up","down","left","right"] ## used to make code make more sense
    path = Stack(1000)  ## stack for path
    path.push(start) ## add start to stack
    while is_connected_to_maze(maze,path.peek()) != True: ## while path is not connected
        pos = path.peek()
        direction = random.choice(directions)
        move_is_valid = True
        if direction == "up":         ## directions 
            new_pos = [pos[0]+1,pos[1]]
        elif direction == "down":
            new_pos = [pos[0]-1,pos[1]]
        elif direction == "left":
            new_pos = [pos[0],pos[1]-1]
        elif direction == "right":
            new_pos = [pos[0],pos[1]+1]
        #print(path.seestack())
        if in_maze(maze,new_pos):    ## checks in maze
            path.push(new_pos)
            for i in range(remove_loop(path)):
                z = path.spop()
    x =  path.seestack() ## return path when connected without hashtags
    len_of_path = x.index("#")
    return x[:len_of_path]
        
    
path = findpath(maze,[0,0])
print(path)

pprint(add_to_maze(path,maze))

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
