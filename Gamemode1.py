import pygame     ## import files
from Wilsons import *
from Backtracking import *


pygame.init()   ## gamemode settings and colours
swidth = 720
sheight = 720   
square_size = 24 
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
        
def load_screen(screen):   ## draws loading screen
    screen.fill(WHITE)
    font = pygame.font.Font("freesansbold.ttf", 50)
    text = font.render("LOADING...",True,BLACK)
    screen.blit(text,(200,300))
    pygame.display.flip()
    


def gamemode1(screen, mazetype):
    len_of_time = 4    ## characters shown on timer
    screen = pygame.display.set_mode((swidth, sheight))  ## initialises screen
    load_screen(screen)
    if mazetype == "Wilsons":      ## generates maze
        maze = WilsonsMazeGen(30) 
    elif mazetype == "Backtracking":
        pygame.event.get()
        maze = backtracking_maze()
        
    player = Player()
    running = True
    won = False
    ctime = 0
    timer = pygame.time.Clock()   ## initialises timer
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  ## checks if game has been quit
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
        timer.tick()
        font = pygame.font.Font("freesansbold.ttf", 50)
        ctime  += ((timer.get_time())/1000)    ## increments timer
        if ctime> 10:
            len_of_time = 5
        screen.fill(WHITE)     ## when finished
        draw_maze(screen, maze)  ## draws maze
        player.draw(screen)
        text2 = font.render(str(ctime)[:len_of_time],True,WHITE)   ## shows timer
        screen.blit(text2,(300,300))   ## draws text on top
        if maze[player.y][player.x] == "2":  ## checks if player has reached goal
            won = True          ## displays win screen
            running = False       
            screen.fill(WHITE)
            font1 = pygame.font.Font("freesansbold.ttf", 30)
            win_string = "You took " + str(ctime)[:len_of_time] + " seconds to complete the maze"   ## win text
            text = font1.render(win_string,True,BLACK)
            screen.blit(text,(40,300))
            pygame.display.flip()
            time.sleep(3)
            return None     ## ends gamemode
        pygame.display.flip()
        
        
   
    
#gamemode1(screen,"Wilsons")   

