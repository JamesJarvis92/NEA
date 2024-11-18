class Node():    ## node class for keeping track of parents and h,g,f cost

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position   ## used for comparing two instances of class

def conv_to_num_array(maze):
    nmaze = []
    for row in maze:
        line = []
        for num in row:
            line.append(int(num))
        nmaze.append(line)
    return nmaze

def A_star(maze, start, end):
    maze = conv_to_num_array(maze)    ## convert to array for algorithm
    print(maze)
    snode = Node(None, start)      
    snode.g = snode.h = snode.f = 0    ## create start node
    enode = Node(None, end)
    enode.g = enode.h = enode.f = 0      ## create end node
    list_of_open = []      ## make open/closed list
    list_of_closed = []
    list_of_open.append(snode)   ## add snode

    while len(list_of_open) > 0:    ## loop until end is found
        current_node = list_of_open[0]    ## gets current node
        current_index = 0
        for index, item in enumerate(list_of_open):
            if item.f < current_node.f:
                current_node = item
                current_index = index
        list_of_open.pop(current_index)       ## pop from open and add to closed
        list_of_closed.append(current_node)

        if current_node == enode:    ## check if finished
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
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

            for onode in list_of_open:    ## if child already on open list
                if child == onode and child.g > onode.g:
                    continue     ## skip rest of iteration

            list_of_open.append(child)   ## add child to open list
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