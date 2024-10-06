import random
from CreateMaze import *
import pygame
import time
pygame.init()
swidth = 720
sheight = 720   
square_size = 24 
mwidth = 30
mheight = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (192, 192, 192)





DIRECTIONS = {"up": (0, -2), "down": (0, 2), "left": (2, 0), "right": (-2, 0)}


def create_maze():
    maze = []
    for i in range(30):
        row = []
        for j in range(30):
            row.append("0")
        maze.append(row)
    return maze

maze = create_maze()

def in_maze(x, y):
    return 0 <= x < 30 and 0 <= y < 30

def make_maze(x, y):
    directions = ["up","down","left","right"]    ## directions to branch to
    random.shuffle(directions)
    
    for direction in directions:
        x_step, y_step = DIRECTIONS[direction]
        new_x, new_y = x + x_step, y + y_step
        if in_maze(new_x, new_y) and maze[new_y][new_x] == "0":
            maze[new_y][new_x] = "1"      ## changes cell 2 in direction
            maze[new_y - y_step // 2][new_x - x_step // 2] = "1"   ## changes cell inbetween current and 2 away
            make_maze(new_x, new_y)
    return maze

def join_maze(maze):
    nmaze = []
    for row in maze:
        nmaze.append("".join(row))
    return nmaze


   
def backtrack_add_end(maze):
    found = False
    end_x = 28
    end_y = 28
    while found == False:
        if maze[end_y][end_x] == "1":
            maze[end_y][end_x] = "2"
            found = True
            return maze
            break
    return maze
            

def backtracking_maze():
    maze = create_maze()
    maze[0][0] = "1"
    maze = make_maze(0,0)
    
    #pprint(maze)
    #print("\n")
    maze = backtrack_add_end(maze)
    maze = join_maze(maze)
    print("z")
    return maze

maze = backtracking_maze()
#pprint(maze)
#print(len(maze),len(maze[0]))




pygame.init()
swidth = 720
sheight = 720   ## change cell size based on size of mazes
square_size = 24 ## need to calculate this based on maze size or just have set sizes for game modes
mwidth = swidth // square_size
mheight = sheight // square_size 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (192, 192, 192)

def draw_maze(screen, maze):
    for y in range(mheight):
        for x in range(mwidth):
            if maze[y][x] == "0":
                pygame.draw.rect(screen, BLACK, (x * square_size, y * square_size, square_size, square_size))  ## draws path
            elif maze[y][x] == "1":
                pygame.draw.rect(screen, RED, (x * square_size, y * square_size, square_size, square_size)) ## draws walls

screen = pygame.display.set_mode((swidth, sheight))
screen.fill(WHITE)
draw_maze(screen,maze)
pygame.display.flip()
time.sleep(3)











