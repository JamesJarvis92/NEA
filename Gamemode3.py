## use manhattan distance for zone 
import pygame
from Wilsons import *

def pprint(maze):
    for i in range(len(maze)):
        print(maze[i])
        
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


def conv_maze(zone_size,maze,player_pos):   ## changes maze to zone around player
    new_maze = []
    for i in range(len(maze)):  ## row
        line = []
        for j in range(len(maze[i])): ## column
            if maze[i][j] == "1":
                manh_dist = abs(player_pos[0]-j) + abs(player_pos[1]-i)  ## could change to pythagoras
                if manh_dist>zone_size:
                   line.append("0")
                else:
                    line.append("1")
            elif maze[i][j] == "0":
                line.append("0")
            else:
                line.append("2")    ## exit
        new_maze.append("".join(line))  
    return new_maze


    




def draw_maze(screen, maze):
    for y in range(mheight):
        for x in range(mwidth):
            if maze[y][x] == "0":
                pygame.draw.rect(screen, BLACK, (x * square_size, y * square_size, square_size, square_size))  ## draws path
            elif maze[y][x] == "1":
                pygame.draw.rect(screen, RED, (x * square_size, y * square_size, square_size, square_size)) ## draws walls



class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
    def move(self, dx, dy, maze):
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < mwidth and 0 <= new_y < mheight and maze[new_y][new_x] != "0":  ## checks square trying to move to is valid
            self.x = new_x    ## assigns new position
            self.y = new_y
    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, (self.x * square_size, self.y * square_size, square_size, square_size))  ##  draws player
        
def load_screen(screen):
    screen.fill(WHITE)
    font = pygame.font.Font("freesansbold.ttf", 50)
    text = font.render("LOADING...",True,BLACK)
    screen.blit(text,(200,300))
    pygame.display.flip()



def gamemode3(screen):
    #screen = pygame.display.set_mode((swidth, sheight))  ## initialises screen
    zone_sizes = [10,8,6,4]
    for size in zone_sizes:
        load_screen(screen)
        maze = WilsonsMazeGen(30) ## need to check maze is solvable with exit
        player = Player()
        running = True
        won = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:    ## does movements 
                    if event.key == pygame.K_UP:
                        player.move(0, -1, maze)
                    elif event.key == pygame.K_DOWN:
                        player.move(0, 1, maze)
                    elif event.key == pygame.K_LEFT:
                        player.move(-1, 0, maze)
                    elif event.key == pygame.K_RIGHT:
                        player.move(1, 0, maze)
                    elif event.key == pygame.K_ESCAPE:
                        return None
            screen.fill(WHITE)     ## when finished
            zoned_maze = conv_maze(size,maze,[player.x,player.y])  ## change zone size
            draw_maze(screen, zoned_maze)  ## draws maze
            player.draw(screen)
            if maze[player.y][player.x] == "2":  ## checks if player has reached goal
                won = True
                running = False
            pygame.display.flip()
        
#screen = pygame.display.set_mode((swidth, sheight))

#gamemode3(screen)