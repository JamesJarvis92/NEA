from Stack import *
from CreateMaze import *  
import random


def is_connected_to_maze(maze,pos):
    connected = False
    try:
        if maze[pos[0]+1][pos[1]] == "1":  ## check down
            connected = True
    except:
        pass
    try:
        if maze[pos[0]-1][pos[1]] == "1": ## check up
            connected = True
    except:
        pass
    try:
        if maze[pos[0]][pos[1]+1] == "1": ## check right
            connected = True
    except:
        pass
    try:
        if maze[pos[0]][pos[1]-1] == "1":  ## check left
            connected = True
    except:
        pass
    return connected


def select_start(maze):
    for i in range(len(maze)**3): ## how many tries to find open node before gives up
        vertlength = len(maze)-1
        horzlength = len(maze[0])-1
        y = random.randint(0,vertlength)   ## selects random squares
        x = random.randint(0,horzlength)
        if maze[y][x] == "0" and is_connected_to_maze(maze,[y,x]) == False: ## checks node is open and not connected to maze
            return [y,x]
    return "END" ## returns if no node is found


def in_maze(maze,pos):
    try:
        x = maze[pos[0]][pos[1]]
        if pos[0]>=0 and pos[1]>=0:
            return True
        else:
            return False
    except:
        return False


def surrounding_nodes(node):
    return [[node[0]-1,node[1]],[node[0]+1,node[1]],[node[0],node[1]-1],[node[0],node[1]+1]]


def remove_loop(stack):
    loop_lengths = [0]
    path = []
    new_pos = stack.spop() ## removes one wanting to be added
    pos2 = stack.spop()   ## removes one before to avoid false loop
    while stack.isEmpty() == False:
        path.append(stack.spop())   ## could use a queue instead
    if len(path)>1:
        path = path[::-1]
    for node in surrounding_nodes(new_pos):
        if node in path:
            x = path.index(node)
            loop_lengths.append(len(path)-x)   ## append lengths of loops
    for node in path:    
        stack.push(node)
    stack.push(pos2)
    stack.push(new_pos)
    return max(loop_lengths)
    
    
def add_to_maze(path,maze): ## add path to maze
    for node in path:
        row = maze[node[0]]
        row = list(row)
        row[node[1]] = "1"
        newrow = "".join(row)
        maze[node[0]] = newrow
    return maze


def findpath(maze,start):
    last_direction = "" ## so it can't go back in itself
    directions = ["up","down","left","right"] ## used to make code make more sense
    path = Stack(1000)  ## stack for path
    path.push(start) ## add start to stack
    while is_connected_to_maze(maze,path.peek()) != True: ## while  path is not connected
        pos = path.peek()
        direction = random.choice(directions)
        move_is_valid = True
        try:                            
            if direction == "up":         ## directions 
                new_pos = [pos[0]-1,pos[1]]
            elif direction == "down":
                new_pos = [pos[0]+1,pos[1]]
            elif direction == "left":
                new_pos = [pos[0],pos[1]-1]
            elif direction == "right":
                new_pos = [pos[0],pos[1]+1]
            if in_maze(maze,new_pos):    ## checks in maze
                path.push(new_pos)
                for i in range(remove_loop(path)):  ## removes loop
                    z = path.spop()
        except:
            pass
    x =  path.seestack() ## return path when connected without hashtags
    len_of_path = x.index("#")
    return x[:len_of_path]
        

def WilsonsMazeGen(size):
    maze = CreateBlankMaze(int(size))
    target_node = [select_start(maze)]  ## first node in form [[y,x]]
    maze = add_to_maze(target_node,maze)  ## adds first node
    done = False
    start_node = [0,0] ## always starts from [0,0]
    while done == False:
        path = findpath(maze,start_node)
        maze = add_to_maze(path,maze)   
        start_node = select_start(maze) ## picks start node
        if start_node == "END": ## checks start node is a node not end
            return maze
        


pprint(add_end(WilsonsMazeGen(12)))




