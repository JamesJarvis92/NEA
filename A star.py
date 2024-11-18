from Priority_Queue import *





maze = ["1000100",
        "1000110",
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

def g_cost(nodes, node):
    path_to_start = dict_path_find(nodes,node)
    g = len(path_to_start)
    return g

#print(g_cost(nodes,(2,2)))

def h_cost(node,end):
    return (abs(node[0]-end[0]) + abs(node[1]-end[1]))

#print(h_cost((2,2),(6,5)))

def f_cost(nodes,node,end):
    try:
        g = g_cost(nodes,node)
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



def A_star(maze, start, end):
    nodes = {}
    start = (start[0],start[1])
    end = (end[0],end[1])
    closed_list = []
    open_list = []
    node = start
    path_found = False
    PQ = PQueue()
    while path_found == False:
        f_cnode = f_cost(nodes, start, end)
        
