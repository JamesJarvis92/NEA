## randomly branch
## check each cell before adding is not connected
## add cell
## once all directions are connected pop from stack and repeat
## add popped cells to maze
## end once stack is empty

import random
from stack import *
from queue import *
from CreateMaze import *

maze = ["200000000",
        "000000000",
        "000000000",
        "000000000",
        "000000000",
        "000000000",
        "000000000",
        "000000000",
        "000000000"]

def is_connected_to_maze(maze,pos): ## checks new node isnt connected to any part of the maze other than previous cell
    connected = 0
    try:
        if maze[pos[0]+1][pos[1]] != "0":  ## check down
            connected += 1
    except:
        pass
    try:
        if maze[pos[0]-1][pos[1]] != "0": ## check up
            connected += 1
    except:
        pass
    try:
        if maze[pos[0]][pos[1]+1] != "0": ## check right
            connected += 1
    except:
        pass
    try:
        if maze[pos[0]][pos[1]-1] != "0":  ## check left
            connected += 1
    except:
        pass
    if connected>1:
        return True
    else:
        return False
    
def add_to_maze(path,maze,symbol): ## add path to maze
    for node in path:
        row = maze[node[0]]
        row = list(row)
        row[node[1]] = str(symbol) ## can add whatever symbol wanted
        newrow = "".join(row)
        maze[node[0]] = newrow
    return maze

def in_maze(maze,pos):
    try:
        x = maze[pos[0]][pos[1]]
        if pos[0]>=0 and pos[1]>=0:
            return True
        else:
            return False
    except:
        return False


def branch(node,maze):
    nodes = Stack(1000)
    nodes.push(node)
    branch_found = False
    while branch_found == False:
        directions = ["up","down","left","right"]
        direction = random.choice(directions)  ## select random direction
        try:
            if direction == "up":            ## checks if direction can be branched to
                new_node = [node[0]-1,node[1]]
                if is_connected_to_maze(maze,node) == False and in_maze(maze,new_node):   ## checks not connected and new node in maze
                    branch_found = True   ## found a branch
                    nodes.push(new_node)    ## add new node stack
                    maze = add_to_maze([new_node],maze,"2")   ## adds unbacktracked cell to maze as "2"
                    
            elif direction == "down":            
                new_node = [node[0]+1,node[1]]
                if is_connected_to_maze(maze,node) == False and in_maze(maze,new_node):  
                    branch_found = True
                    nodes.push(new_node)
                    maze = add_to_maze([new_node],maze,"2")
                    
            if direction == "left":           
                new_node = [node[0],node[1]-1]
                if is_connected_to_maze(maze,node) == False and in_maze(maze,new_node):  
                    branch_found = True
                    nodes.push(new_node)
                    maze = add_to_maze([new_node],maze,"2")
                    
            if direction == "right":           
                new_node = [node[0],node[1]+1]
                if is_connected_to_maze(maze,node) == False and in_maze(maze,new_node):  
                    branch_found = True
                    nodes.push(new_node)
                    maze = add_to_maze([new_node],maze,"2")
               
            directions.remove(direction)
                    
        except:                         ## if the direction isn't in maze direction is removed from list
            directions.remove(direction)
            
        if len(directions) == 0: ## if no direction is valid breaks loop
            break
    print(nodes.peek())
    if branch_found == False:
        backtrack_node = nodes.spop()
        maze = add_to_maze([add_node],maze,"1")  ## shows cell has been backtracked by changing it to a 1
    #if nodes.isEmpty() == True:
        #return maze
    pprint(maze)
    print(direction)
    branch(nodes.peek(),maze)
        

print(branch([0,0],maze))
print("x")        
            


# https://stackoverflow.com/questions/60532245/implementing-a-recursive-backtracker-to-generate-a-maze
## read
    
