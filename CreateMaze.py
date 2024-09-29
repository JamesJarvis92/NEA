import random

def CreateBlankMaze(size):   ## creates 2D array of 0's
    maze = []
    for i in range(size):
        maze.append("0"*size)
    return maze

def CreateBlankMazeList(size):   ## creates 2D array of 0's
    maze = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append("0")
        maze.append(row)
    return maze



def pprint(maze):
    for i in range(len(maze)):
        print(maze[i])


def add_end(maze):  ## works for maze with 1's and 0's
    size = len(maze)-1
    end_range = len(maze)//5 ## change how close to bottom right end is
    found = False
    while found == False:
        end_y = size - (random.randint(0,end_range))
        end_x = size - (random.randint(0,end_range))
        if maze[end_y][end_x] == "1": ## checks goal would be in maze
            found = True
            row = list(maze[end_y])  
            row[end_x] = "2"
            row = "".join(row)
            maze[end_y] = row ## adds goal to maze
            return maze

            

""" ## not top priority
def conv_to_image_array(maze):  ## turn maze into array of codes so can draw maze using pixel art
    img_array = []
    codes = {"U":1, "D":2, "L":3, "R":4, "UR":5, "UD":6, "UL":7, "RD":8, "RL":9, "DL":10, "URD":11, "URL":12, "UDL":13, "RDL":14, "URDL":15}  ## when worked out which walls each cell has will append code to array
    for row in maze:   ## makes nested list of required length
        img_array.append([])
        
        
   ## go around clockwise starting from up to check if wall and append to string if there is a wall
"""