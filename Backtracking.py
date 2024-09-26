import random
from CreateMaze import *
import pygame
import time
pygame.init()
swidth = 720
sheight = 720   ## change cell size based on size of mazes
square_size = 24 ## need to calculate this based on maze size or just have set sizes for game modes
mwidth = 30#swidth // square_size
mheight = 30#sheight // square_size 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (192, 192, 192)

# Constants for the maze dimensions
WIDTH = 30  # Must be odd
HEIGHT = 30  # Must be odd

# Characters for displaying the maze
EMPTY = '1'
WALL = '0'

# Directions
NORTH, SOUTH, EAST, WEST = 'N', 'S', 'E', 'W'
DIRECTIONS = {NORTH: (0, -2), SOUTH: (0, 2), EAST: (2, 0), WEST: (-2, 0)}

# Initialize the maze with walls
maze = [[WALL for _ in range(WIDTH)] for _ in range(HEIGHT)]



def in_maze(x, y):
    return 0 <= x < WIDTH and 0 <= y < HEIGHT

def make_maze(x, y):
    directions = list(DIRECTIONS.keys())
    random.shuffle(directions)
    
    for direction in directions:
        x_step, y_step = DIRECTIONS[direction]
        new_x, new_y = x + x_step, y + y_step
        if in_maze(new_x, new_y) and maze[new_y][new_x] == "0":
            maze[new_y][new_x] = EMPTY
            maze[new_y - y_step // 2][new_x - x_step // 2] = EMPTY
            make_maze(new_x, new_y)
            
def remove_edges(maze):
    maze = maze[1:]
    for row in maze:
        row = row[1:]
    return maze

# Start the maze generation from the top-left corner
maze[1][1] = "1"
make_maze(1, 1)
pprint(maze)
#maze = remove_edges(maze)
screen = pygame.display.set_mode((swidth, sheight))
# Print the generated maze
#pprint(maze)

def draw_maze(screen, maze):
    for y in range(mheight):
        for x in range(mwidth):
            if maze[y][x] == "0":
                pygame.draw.rect(screen, BLACK, (x * square_size, y * square_size, square_size, square_size))  ## draws path
            elif maze[y][x] == "1":
                pygame.draw.rect(screen, RED, (x * square_size, y * square_size, square_size, square_size)) ## draws walls
    pygame.display.flip()
    time.sleep(15)
                
draw_maze(screen,maze)




