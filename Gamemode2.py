import pygame
from Wilsons import *

pygame.init()
swidth = 720
sheight = 720   ## change cell size based on size of mazes
square_size = 24 ## need to calculate this based on maze size or just have set sizes for game modes
mwidth = swidth // square_size
mheight = sheight // square_size 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = ((0,0,255))
RED = (255, 0, 0)
GRAY = (192, 192, 192)

#screen = pygame.display.set_mode([720,720])

def draw_maze(screen, maze):
    for y in range(mheight):
        for x in range(mwidth):
            if maze[y][x] == "0":
                pygame.draw.rect(screen, BLACK, (x * square_size, y * square_size, square_size, square_size))  ## draws path
            elif maze[y][x] == "1":
                pygame.draw.rect(screen, RED, (x * square_size, y * square_size, square_size, square_size)) ## draws walls



class Player:
    def __init__(self,color):
        self.color = color
        self.x = 0
        self.y = 0
    def move(self, dx, dy, maze):
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < mwidth and 0 <= new_y < mheight and maze[new_y][new_x] != "0":  ## checks square trying to move to is valid
            self.x = new_x    ## assigns new position
            self.y = new_y
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x * square_size, self.y * square_size, square_size, square_size))  ##  draws player
        

def gamemode2(screen):
    #screen = pygame.display.set_mode((swidth, sheight))  ## initialises screen
    maze = add_end(WilsonsMazeGen(30)) ## need to check maze is solvable with exit
    player1 = Player(GREEN)
    player2 = Player(BLUE)
    running = True
    #won = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:    ## does movements 
                if event.key == pygame.K_UP:
                    player1.move(0, -1, maze)
                elif event.key == pygame.K_DOWN:
                    player1.move(0, 1, maze)
                elif event.key == pygame.K_LEFT:
                    player1.move(-1, 0, maze)
                elif event.key == pygame.K_RIGHT:
                    player1.move(1, 0, maze)
                elif event.key == pygame.K_w:
                    player2.move(0, -1, maze)
                elif event.key == pygame.K_s:
                    player2.move(0, 1, maze)
                elif event.key == pygame.K_a:
                    player2.move(-1, 0, maze)
                elif event.key == pygame.K_d:
                    player2.move(1, 0, maze)
        screen.fill(WHITE)     ## when finished
        draw_maze(screen, maze)  ## draws maze
        player1.draw(screen)
        player2.draw(screen)
        if maze[player1.y][player1.x] == "2":  ## checks if player has reached goal
            winner = 1
            running = False
        elif maze[player2.y][player2.x] == "2":
            winner = 2
            running = False
        pygame.display.flip()
    return winner
#print(gamemode2(screen))