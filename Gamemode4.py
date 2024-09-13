import pygame
import time 

pygame.init()
swidth = 720
sheight = 720   ## change cell size based on size of mazes
square_size = 90 ## need to calculate this based on maze size or just have set sizes for game modes
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
    def __init__(self,color,pos):
        self.color = color
        self.x = pos[1]
        self.y = pos[0]
    def move(self, dx, dy, maze):
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < mwidth and 0 <= new_y < mheight and maze[new_y][new_x] != "0":  ## checks square trying to move to is valid
            self.x = new_x    ## assigns new position
            self.y = new_y
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x * square_size, self.y * square_size, square_size, square_size))  ##  draws player
        
        
def load_screen(screen):
    screen.fill(WHITE)
    font = pygame.font.Font("freesansbold.ttf", 50)
    text = font.render("LOADING...",True,BLACK)
    screen.blit(text,(200,300))
    pygame.display.flip()
    
screen = pygame.display.set_mode((swidth, sheight))

maze = ["10000010",
        "10111010",
        "10001010",
        "11111110",
        "10010010",
        "11111010",
        "10000010",
        "11002110"]

enemy_moves = [[0,1],[0,1],[0,1],[0,1],[0,1],[0,1]] ## use queue for moves and then dequeue front

def gamemode1(screen,maze,enemy_moves):
    screen = pygame.display.set_mode((swidth, sheight))  ## initialises screen
    load_screen(screen)
    #maze = WilsonsMazeGen(30) ## need to check maze is solvable with exit
    player = Player(GREEN,[0,0])
    enemy1 = Player(GRAY,[0,6])
    running = True
    won = False
    timer = pygame.time.Clock()
    ms = 0
    while running:
        emove = 0
        ms += timer.get_time()  ## add time since last tick to ms
        print(ms)
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
        if len(enemy_moves)>0 and ms>1000:   ## checks how many milliseconds since last call
            enemymove = enemy_moves[emove]
            enemy1.move(enemymove[0],enemymove[1], maze)
            enemy_moves.pop(0)
            ms = 0  ## resets time between enemy moves
        timer.tick()  ## increases timer
        screen.fill(WHITE)     ## when finished
        draw_maze(screen, maze)  ## draws maze
        player.draw(screen)
        enemy1.draw(screen)
        if maze[player.y][player.x] == "2":  ## checks if player has reached goal
            won = True
            running = False
        pygame.display.flip()
        
        
   
    
gamemode1(screen,maze,enemy_moves)   