
##### find way to remove duplicates from pqueue #######   or just cut list after 50 vals or something


from CreateMaze import *
from Priority_Queue import *

class Node():    ## node class for keeping track of parents and h,g,f cost

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    #def __eq__(self, other):
        #return self.position == other.position   ## used for comparing two instances of class

def conv_to_num_array(maze):      ## turns into array of integers and changes end to a 1
    nmaze = []
    for row in maze:
        line = []
        for num in row:
            if num == "2":
                line.append(1)
            else:
                line.append(int(num))
            
        nmaze.append(line)
    return nmaze

def A_star(maze, start, end):
    try:
        start.append("x")
        start = (start[0],start[1])
    except:
        pass
    try:
        end.append("x")
        end = (end[0],end[1])
    except:
        pass
    positions_in_open = []
    maze = conv_to_num_array(maze)    ## convert to array for algorithm
    #pprint(maze)
    #print(start,end)
    snode = Node(None, start)      
    snode.g = snode.h = snode.f = 0    ## create start node
    enode = Node(None, end)
    enode.g = enode.h = enode.f = 0      ## create end node
    list_of_open = PQueue()     ## make open/closed list
    positions_in_open.append(snode.position)
    list_of_closed = []
    snode = Builder(snode,snode.f)
    list_of_open.insert(snode)   ## add snode

    while list_of_open.size() > 0:    ## loop until end is found
        
        
        current_node = list_of_open.frontval()    ## gets current node
        #print(current_node.position)
        current_index = 0
        #list_of_open = list_of_open[:50]
        #print(list_of_open.size())
        current_node = list_of_open.delete()
        #print(current_node.position)
        
        #print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        list_of_closed.append(current_node)

        if current_node.position == enode.position:    ## check if finished
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            #print("done")
            return path[::-1]  ## returns path from start to end

        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: ## moves around cell
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])   ## find node position
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:   ## check node in maze
                continue   ## skip rest of iteration 
            if maze[node_position[0]][node_position[1]] != 1:   ## check cell is path
                continue    ## skip rest of iteration
            new_node = Node(current_node, node_position)   ## new node
            children.append(new_node)  ## add new node to children

        
        for child in children:
            for closed_child in list_of_closed:    ## if child on closed list
                if child == closed_child:
                    continue   ## skip rest of iteration

            child.g = current_node.g + 1     ## set g val
            child.h = ((child.position[0] - enode.position[0]) ** 2) + ((child.position[1] - enode.position[1]) ** 2)    ## set h val
            child.f = child.g + child.h    ## set f val

            for onode in list_of_open.getlist():    ## if child already on open list
                if child == onode and child.g > onode.g:
                    continue     ## skip rest of iteration
            nnode = Builder(child, child.f)
            if nnode.data.position not in positions_in_open:
                list_of_open.insert(nnode)   ## add child to open list
                positions_in_open.append(nnode.data.position)
            else:
                pass
    return False

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


nmaze = [[1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
[0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
[1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
[0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1],
[0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
[0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
[0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
[0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1],
[0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1],
[0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0],
[1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
[0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1],
[0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1],
[0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1],
[0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1],
[0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
[0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1],
[0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
[0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1],
[0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
[1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1],
[1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1],
[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
[1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0],
[1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1],
[1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1]]

"""
nmaze = [[1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1],
    [1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1],
    [1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1],
    [1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1]]

nmaze = [[1,0,1,1,1],
         [1,0,1,0,1],
         [1,1,1,0,1],
         [1,1,1,0,1],
         [1,1,1,0,1]]
    """     
nmaze = ["101000011000001111100000001011",
"101000010011100011001111101010",
"101011110010101101001000111011",
"101110001110101001001110100001",
"110101111010101001111001101111",
"011110010010001010101001001010",
"011010010011111011111001100110",
"101100000101001000010010000111",
"111111111111101000101010110100",
"011110000010101011101111100111",
"001011000110101110011101111101",
"001101110010100011110101100100",
"110011000111100010010000100110",
"011011110101001110011111100010",
"001111011001001011000010011011",
"001001001110011000100110101001",
"001001100001111011111100111001",
"001010111111001001000001101001",
"101110010100000011101100011001",
"111101110101110010100101111110",
"000101000000110010111110010010",
"011011111110100000101101010010",
"111010010011111111100101010010",
"111110010000100000000101110010",
"100010011100100100110111000020",
"011111100011110101100100111110",
"010010111010011111110101100100",
"010000100011000100010100000111",
"011101110001110111010111111001",
"110111011111011001010000001101"]
#print(conv_to_num_array(nmaze))
start = [0, 0]
end = [24, 28]

path = A_star(nmaze, start, end)
print(path)
print(conv_to_moves(path))



