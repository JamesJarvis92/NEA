import pygame             ## import files, settings, colours
import time as t
import random
from Backtracking import *
from Wilsons import *
from DFS import *
from A_star import *
pygame.init()
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

def draw_maze(screen, maze):       ## draw maze
    for y in range(mheight):
        for x in range(mwidth):
            if maze[y][x] == "0":
                pygame.draw.rect(screen, BLACK, (x * square_size, y * square_size, square_size, square_size))  ## draws path
            elif maze[y][x] == "1":
                pygame.draw.rect(screen, RED, (x * square_size, y * square_size, square_size, square_size)) ## draws walls
            elif maze[y][x] == "x":
                pygame.draw.rect(screen, RED, (x * square_size, y * square_size, square_size, square_size))   ## draws paths


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
            return True
        else:
            return False

    def draw(self, screen):  ## draws player
        pygame.draw.rect(screen, self.color, (self.x * square_size, self.y * square_size, square_size, square_size))  ##  draws player
        
        
def load_screen(screen):   ## draws loading screen
    screen.fill(WHITE)
    font = pygame.font.Font("freesansbold.ttf", 50)
    text = font.render("LOADING...",True,BLACK)
    screen.blit(text,(200,300))
    pygame.display.flip()
    
def back_to_org(maze):    ## converts maze back to original format
    nmaze = []
    for row in maze:
        nrow = ""
        for letter in row:
            if letter == "0":
                nrow += "0"
            else:
                nrow += "1"
        nmaze.append(nrow)
    return nmaze

def find_enemy_start(maze):   ## finds start position enemy randomly from list of possible positions
    starts = [[0,25],[0,26],[0,27],[0,28],[1,25],[1,26],[1,27],[1,28],[2,25],[2,26],[2,27],[2,28],[25,0],[26,0],[27,0],[28,0],[25,1],[26,1],[27,1],[28,1],[25,2],[26,2],[27,2],[28,2]]
    while True:
        start = random.choice(starts)
        if maze[start[0]][start[1]] == "1":
            return start
    
def gamemode4(screen, mazetype, pathtype):
    lost = False
    times = [500,400,300,250,200]
    rounds = ["1","2","3","4","5"]
    screen = pygame.display.set_mode((swidth, sheight))  ## initialises screen
    for time in times:
        if lost == False:
            screen.fill(WHITE)    ## round number screen
            font = pygame.font.Font("freesansbold.ttf", 50)
            string = "Round " + rounds[0]
            text = font.render(string,True,BLACK)
            screen.blit(text,(200,300))
            pygame.display.flip()
            t.sleep(1)
            rounds.pop(0)
            while True:
                try:
                    if mazetype == "Wilsons": ## generates maze
                        maze = WilsonsMazeGen(30) 
                    elif mazetype == "Backtracking":
                        maze = backtracking_maze()
                    end = find_end(maze)    ## finds end of maze
                    estart = find_enemy_start(maze)   ## finds enemy start position
                    player = Player(GREEN,[0,0])   ## initialises player, enemy
                    enemy1 = Player(GRAY, estart)   
                    if pathtype == "DFS":    ## find enemy path
                        enemy_moves = dfs(maze,[enemy1.y,enemy1.x],[player.y,player.x])
                    elif pathtype == "A*":
                        enemy_moves = A_star(maze,[enemy1.y,enemy1.x],[player.y,player.x])
                    esteps = conv_to_moves(enemy_moves)   ## change enemy path to steps
                    break
                except:
                    pass
            running = True
            won = False
            timer = pygame.time.Clock()
            t1 = 0
            t2 = 0
            moved = False
            while running:
                emove = 0
                t1 += timer.get_time()  ## add time since last tick to ms
                t2 += timer.get_time()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:    ## does movements 
                        if event.key == pygame.K_UP:
                            player.move(0, -1, maze)
                            moved = True
                        elif event.key == pygame.K_DOWN:
                            player.move(0, 1, maze)
                            moved = True
                        elif event.key == pygame.K_LEFT:
                            player.move(-1, 0, maze)
                            moved = True
                        elif event.key == pygame.K_RIGHT:
                            player.move(1, 0, maze)
                            moved = True
                        elif event.key == pygame.K_ESCAPE:
                            return None
                if [player.x,player.y] == [enemy1.x,enemy1.y]:  ## checks if enemy is on player
                    screen.fill(WHITE)  ## loss screen
                    font = pygame.font.Font("freesansbold.ttf", 50)
                    text = font.render("You lost :(",True,BLACK)
                    screen.blit(text,(200,300))
                    pygame.display.flip()
                    t.sleep(1)
                    running = False
                    return None
                    
                if t1>time:   ## checks how many milliseconds since last call
                    try:
                        step = esteps[0]
                        enemy1.move(step[1],step[0],maze)
                        esteps.pop(0)
            
                        t1 = 0  ## resets time between enemy moves
                    except:
                        lost = True
                        running = False
                if t2>1000:
                    if moved:
                        ppos = [player.y,player.x]
                        epos = [enemy1.y,enemy1.x]
                        if pathtype == "DFS":    ## recalculates enemy path once player has moved
                            enemy_moves = dfs(back_to_org(maze),epos,ppos)
                        elif pathtype == "A*":
                            enemy_moves = A_star(back_to_org(maze),epos,ppos)
                        esteps = conv_to_moves(enemy_moves)   ## changes path to steps
                        moved = False
                    
                    t2 = 0
                    
            
                timer.tick()  ## increases timer
                screen.fill(WHITE)     ## when finished
                try:
                    draw_maze(screen, maze)  ## draws maze
                    player.draw(screen)
                    enemy1.draw(screen)
                    if maze[player.y][player.x] == "2" and rounds == []:  ## checks if player has reached goal of final round
                        screen.fill(WHITE)  ## win screen
                        font = pygame.font.Font("freesansbold.ttf", 50)
                        text = font.render("You won :)",True,BLACK)
                        screen.blit(text,(200,300))
                        pygame.display.flip()
                        t.sleep(1)
                        won = True
                        running = False
                    elif maze[player.y][player.x] == "2":
                        running = False
                
                    
                    pygame.display.flip()
                
                except:
                    pass
                
       
   
#gamemode4(screen)   