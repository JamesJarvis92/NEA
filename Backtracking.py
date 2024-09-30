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


   


def backtracking_maze():
    maze = create_maze()
    maze[0][0] = "1"
    maze = make_maze(0,0)
    maze = join_maze(maze)
    pprint(maze)
    print("\n")
    maze = add_end(maze)
    pprint(maze)
    return maze

maze = backtracking_maze()
print(len(maze),len(maze[0]))









