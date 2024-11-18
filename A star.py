from Priority_Queue import *





maze = ["1110100",
        "100110",
        "1010100",
        "1111111",
        "0010010",
        "1110010",
        "0010012"]


#nodes = {(0,1):(0,0),(1,1):(0,1), (2,1):(1,1), (2,2):(2,1)}

def dict_path_find(nodes, end_node):
    path = []
    node = nodes[end_node]
    path.append(node)
    while node != (0,0):
        new_node = nodes[node]
        path.append(new_node)
        node = new_node
    return path[::-1]

#print(dict_path_find(nodes,(2,2)))
"""
def g_cost(nodes, node):
    path_to_start = dict_path_find(nodes,node)
    g = len(path_to_start)
    return g
"""
def g_cost(node,start):
    return (abs(node[0]-start[0]) + abs(node[1]-start[1]))

#print(g_cost(nodes,(2,2)))

def h_cost(node,end):
    return (abs(node[0]-end[0]) + abs(node[1]-end[1]))

#print(h_cost((2,2),(6,5)))

def f_cost(nodes,node,end,start):
    try:
        g = g_cost(start,node)
    except:
        g = 0
    try:
        h = h_cost(node,end)
    except:
        h = 0
    return g+h

#print(f_cost(nodes,(2,2),(6,5)))

def find_end(maze):
    for i in range(len(maze)):
        row = list(maze[i])
        if "2" in row:
            return (i,row.index("2"))
        
#print(find_end(maze))

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


def find_move(maze,pos,closed_list):
    vnodes = []
    try:
        if maze[pos[0]+1][pos[1]] == "1":  ## check down
            vnodes.append(((pos[0]+1),pos[1]))
    except:
        pass
    try:
        if maze[pos[0]][pos[1]-1] == "1" and (pos[1]-1)>=0: ## check left
            vnodes.append((pos[0],(pos[1]-1)))
    except:
        pass
    try:
        if maze[pos[0]-1][pos[1]] == "1" and (pos[0]-1)>=0: ## check up
            vnodes.append(((pos[0]-1),pos[1]))
    except:
        pass
    try:
        if maze[pos[0]][pos[1]+1] == "1":  ## check right
            vnodes.append((pos[0],(pos[1]+1)))
    except:
        pass
    return vnodes
    anodes = []
    for node in vnodes:
        if node in closed_list:
            pass
        else:
            anodes.append(node)

    if anodes == []:
        return False
    
    return anodes



def A_star(maze, start, end):
    nodes = {}
    start = (start[0],start[1])
    end = (end[0],end[1])
    closed_list = []
    open_list = []
    open_list = PQueue()
    cnode = Builder(start,0)
    open_list.insert(cnode)
    closed_list.append(open_list.getlist()[0][0])
    open_list.delete()
    while True:
        if connected_to_end(maze,cnode):
            nodes[end] = cnode
            return nodes
        try:
            print(find_move(maze,cnode,closed_list))
            for node in find_move(maze,cnode,closed_list):
                nodes[node] = cnode
                PQnode = Builder(node,f_cost(nodes,node,end,start))
                open_list.insert(PQnode)
            cnode = open_list.delete()
        except:
            nodes[cnode] = end
            return nodes
        
        
print(A_star(maze,(0,0),(6,6)))

#closed_list = [(0,0)]
#print(find_move(maze,(0,0),closed_list))