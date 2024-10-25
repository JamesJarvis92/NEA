from DataStructures import *

maze = ["10000010",
        "10111010",
        "10001010",
        "11111110",
        "10010010",
        "11111010",
        "10000010",
        "11002110"]

def find_move(maze,pos):
    try:
        if maze[pos[0]+1][pos[1]] == "1":  ## check down
            return [(pos[0]+1),pos[1]]
    except:
        pass
    try:
        if maze[pos[0]][pos[1]-1] == "1" and (pos[1]-1)>=0: ## check left
            return [pos[0],(pos[1]-1)]
    except:
        pass
    try:
        if maze[pos[0]-1][pos[1]] == "1" and (pos[0]-1)>=0: ## check up
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

        
def find_end(maze):
    for i in range(len(maze)):
        row = list(maze[i])
        if "2" in row:
            return [i,row.index("2")]


def dfs(maze,start,end):
    nmaze = maze
    path = Stack(500)
    path.push(start)
    path_found = False
    nmaze = add_x(nmaze,path.peek())
    while path_found == False and path.isEmpty() == False:
        if path.peek() == end:
            path_found = True
            return path.seestack()    ## returns path when end = "1"
        next_move = find_move(nmaze,path.peek())    ## push next move unless no move then pop until there is a move
        if next_move == False:   ## if no move backtracks until there is an available move
            path.spop()
        else:
            path.push(next_move)
            nmaze = add_x(nmaze,next_move)   ## shows cell as visited
        if connected_to_end(nmaze,next_move):
            path.push(end)
            x =  path.seestack() ## return path when connected without hashtags
            len_of_path = x.index("#")
            return x[:len_of_path]
                ## returns path when end = "2"
            

    return False    ## returns when no path
          


def conv_to_moves(moves):
    steps = []
    for i in range(len(moves)):
        try:
            ych = moves[i+1][0] - moves[i][0]
        except:
            pass
        try:
            xch = moves[i+1][1] - moves[i][1]
        except:
            pass
        steps.append([ych,xch])
    return steps

