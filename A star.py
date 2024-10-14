from Priority_Queue import *
from CreateMaze import *
import pygame
import time
 
def manhattan_dist(pos1,pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1]) 
    
def possible_moves(pos,path,maze):
    
    positions = []
    try:
        if maze[pos[0]+1][pos[1]] == "1":  ## check down
            positions.append([pos[0]+1,pos[1]])
    except:
        pass
    try:
        if maze[pos[0]-1][pos[1]] == "1": ## check up
            positions.append([pos[0]-1,pos[1]])
    except:
        pass
    try:
        if maze[pos[0]][pos[1]+1] == "1": ## check right
            positions.append([pos[0],pos[1]+1])
    except:
        pass
    try:
        if maze[pos[0]][pos[1]-1] == "1":  ## check left
            positions.append([pos[0],pos[1]-1])
    except:
        pass
    return positions
    
    vpositions = []
    for pos in positions:  ## checks node not visited yet
        if pos in path:
            pass
        else:
            vpositions.append(pos)
    return vpositions
    

maze = ["100000000",
        "101111110",
        "101001000",
        "111001111",
        "001111001",
        "001001000",
        "011001000",
        "001001111",
        "001000001"]

def A_star(maze,start,end):
    path_found = False
    path = []
    cnode = start
    while path_found == False:
        queue = PQueue()
        nodes = possible_moves(cnode,path,maze)
        if len(nodes) == 0:
            nodes.pop(0)
        
        for node in nodes:
            print(node)
            time.sleep(1)
            g = manhattan_dist(node,start)
            h = manhattan_dist(node,end)
            f = g + h
            queue_pos = Builder(node,f)
            queue.insert(queue_pos)
        cnode = queue.getlist()[0][0]
        print(cnode)
        if cnode == end:
            path.append(end)
            return path
        path.append(cnode)

print(A_star(maze,[0,0],[8,8]))   
#print(possible_moves([0,0],[],maze))        
        


