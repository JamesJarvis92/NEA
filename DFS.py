from stack import *

maze = ["10000010",
        "10111010",
        "10001010",
        "11111110",
        "10010010",
        "11111010",
        "10000010",
        "11001110"]

def find_move(maze,pos):
    try:
        if maze[pos[0]+1][pos[1]] == "1":  ## check down
            return [(pos[0]+1),pos[1]]
    except:
        pass
    try:
        if maze[pos[0]][pos[1]-1] == "1": ## check left
            return [pos[0],(pos[1]-1)]
    except:
        pass
    try:
        if maze[pos[0]-1][pos[1]] == "1": ## check up
            return [(pos[0]-1),pos[1]]
    except:
        pass
    try:
        if maze[pos[0]][pos[1]+1] == "1":  ## check right
            return [pos[0],(pos[1]+1)]
    except:
        pass
    return False

def connected_to_end(maze,pos):
    try:
        if maze[pos[0]+1][pos[1]] == "2":  ## check down
            return True
    except:
        pass
    try:
        if maze[pos[0]][pos[1]-1] == "2": ## check left
            return True
    except:
        pass
    try:
        if maze[pos[0]-1][pos[1]] == "2": ## check up
            return True
    except:
        pass
    try:
        if maze[pos[0]][pos[1]+1] == "2":  ## check right
            return True
    except:
        pass
    return False

def add_x(maze,pos):
    try:
        row = maze[pos[0]]
        row = list(row)
        row[pos[1]] = "x"
        newrow = "".join(row)
        maze[pos[0]] = newrow
    except:
        pass
    return maze
#print(add_x(maze,[0,0]))
    

#print(connected_to_end(maze,[7,5]))
def dfs(maze,start,end):
    path = Stack(500)
    path.push(start)
    path_found = False
    maze = add_x(maze,path.peek())
    while path_found == False and path.isEmpty() == False:
        if path.peek() == end:
            path_found = True
            return path.seestack()    ## returns path when end = "1"
        next_move = find_move(maze,path.peek())    ## push next move unless no move then pop until there is a move
        if next_move == False:   ## if no move backtracks until there is an available move
            path.spop()
        else:
            path.push(next_move)
            maze = add_x(maze,next_move)   ## shows cell as visited
        if connected_to_end(maze,next_move):
            path.push(end)
            return path.seestack()    ## returns path when end = "2"
            

    return False    ## returns when no path
          
print(dfs(maze,[0,0],[7,4]))