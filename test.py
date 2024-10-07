from stack import *
from CreateMaze import *
import random
## install pygame by tools, python, python environment

class Cell:
    def init(self, xpos, ypos, pathchar):
        self.xpos = xpos
        self.ypos = ypos
        self.pathchar = pathchar
     
    def get_pos(self):
        return [self.ypos,self.xpos]
    
    def get_pathchar(self):
        return self.pathchar
    
    def change_pathchar(self, char):
        self.pathchar = char

class WilsonsMaze:
    def init(self,size):
        self.size = size
        self.stack = Stack(1000)





    def is_connected_to_maze(self,maze,cell):
        pos = cell.get_pos()
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


    def select_start(self, maze):
        for i in range(len(maze)**3): ## how many tries to find open node before gives up
            vertlength = self.size - 1
            horzlength = self.size - 1
            y = random.randint(0,vertlength)   ## selects random squares
            x = random.randint(0,horzlength)
            start_cell = maze[y][x]
            if start_cell.get_pathchar() == "0" and WilsonsMaze.is_connected_to_maze(maze,start_cell)
                return start_cell.get_pos()
        return "END" ## returns if no node is found


    def in_maze(self, maze,cell):
        pos = cell.get_pos()
        try:
            x = maze[pos[0]][pos[1]]
            if pos[0]>=0 and pos[1]>=0:
                return True
            else:
                return False
        except:
            return False


    def surrounding_nodes(self, node_pos):
        return [[node_pos[0]-1,node_pos[1]],[node_pos[0]+1,node_pos[1]],[node_pos[0],node_pos[1]-1],[node_pos[0],node_pos[1]+1]]


    def remove_loop(self):
        loop_lengths = [0]
        path = []
        new_pos = self.stack.spop() ## removes one wanting to be added
        pos2 = self.stack.spop()   ## removes one before to avoid false loop
        while self.stack.isEmpty() == False:
            path.append(self.stack.spop())   
        if len(path)>1:
            path = path[::-1]
        for node in WilsonsMaze.surrounding_nodes(new_pos):
            if node in path:
                x = path.index(node)
                loop_lengths.append(len(path)-x)   ## append lengths of loops
        for node in path:    
            self.stack.push(node)
        self.stack.push(pos2)
        self.stack.push(new_pos)
        return max(loop_lengths)
    
    
    def add_to_maze(path,maze): ##### change this probably
        for cell in path:
            cell.change_pathchar("1")
        


    def findpath(self,maze,start_cell):
        last_direction = "" ## so it can't go back in itself
        directions = ["up","down","left","right"] ## used to make code make more sense
        self.stack.push(start_cell) ## add start to stack
        while WilsonsMaze.is_connected_to_maze(maze,self.stack.peek()) != True: ## while  path is not connected
            ccell = self.stack.peek()
            pos = ccell.get_pos()
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
                if WilsonsMaze.in_maze(maze,new_pos):    ## checks in maze
                    self.stack.push(new_pos)
                    for i in range(WilsonsMaze.remove_loop(self.stack)):  ## removes loop
                        z =self.stack.spop()
            except:
                pass
        x =  self.stack.seestack() ## return path when connected without hashtags
        len_of_path = x.index("#")
        return x[:len_of_path]
        

def WilsonsMazeGen(self,size):
    ## make maze out of cell class
    start_cell = [WilsonsMaze.select_start(maze)]  ## first node in form [[y,x]]
    maze = WilsonsMaze.add_to_maze(start_cell,maze)  ## adds first node
    done = False
    start_node = maze[0,0].get_pos() ## always starts from [0,0]
    while done == False:
        path = WilsonsMaze.findpath(maze,start_node)
        maze = add_to_maze(path,maze)   
        start_node = select_start(maze) ## picks start node
        if start_node == "END": ## checks start node is a node not end
            maze = add_end(maze)
            return maze