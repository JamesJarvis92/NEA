import pygame
from Backtracking import *
from Wilsons import *
from DFS import *       ## import files and set settings, colours
from A_star import *
import time as t
from Queue import *
pygame.init()
swidth = 720
sheight = 720   
square_size = 24 
mwidth = swidth // square_size
mheight = sheight // square_size 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = ((0,0,255))
RED = (255, 0, 0)
GRAY = (192, 192, 192)
ORANGE = ((255,100,10))
font = pygame.font.Font("freesansbold.ttf", 24)
screen = pygame.display.set_mode([720,720])

class Button:
    def __init__(self,txt,pos,mcol,ocol,textcol):  ## initialises button
        self.text = txt
        self.pos = pos
        self.mcol = mcol
        self.ocol = ocol
        self.textcol = textcol
        self.button = pygame.rect.Rect((self.pos[0],self.pos[1]),(260,40))
    
    def draw(self,screen):    ## draws button
        btn = pygame.draw.rect(screen, self.mcol, self.button,0,5)
        pygame.draw.rect(screen, self.ocol, self.button,5,5)
        font = pygame.font.Font("freesansbold.ttf", 24)
        text = font.render(self.text,True,self.textcol)
        screen.blit(text,(self.pos[0]+15,self.pos[1]+7))
        
    def check_clicked(self):        ## checks if clicked
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False
        
    def hovering(self):     ## checks if hovering
        if (self.button).collidepoint(pygame.mouse.get_pos()):
            temp = self.mcol
            self.mcol = self.ocol
            self.ocol = temp
        
def draw_maze(screen, maze):    ## draws maze
    for y in range(mheight):
        for x in range(mwidth):
            if maze[y][x] == "0":
                pygame.draw.rect(screen, BLACK, (x * square_size, y * square_size, square_size, square_size))  ## draws path
            elif maze[y][x] == "1":
                pygame.draw.rect(screen, RED, (x * square_size, y * square_size, square_size, square_size)) ## draws walls
            elif maze[y][x] == "x":
                pygame.draw.rect(screen, RED, (x * square_size, y * square_size, square_size, square_size))



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

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x * square_size, self.y * square_size, square_size, square_size))  ##  draws player
        
def load_screen(screen):     ## draws load screen
    screen.fill(WHITE)
    font1 = pygame.font.Font("freesansbold.ttf", 50)
    text = font1.render("LOADING...",True,BLACK)
    screen.blit(text,(200,300))
    pygame.display.flip()
    


def two_player_mode(screen, mazetype):
    load_screen(screen)
    if mazetype == "Wilsons":   ## generates maze
        maze = WilsonsMazeGen(30)  
    elif mazetype == "Backtracking":
        maze = backtracking_maze()
    player1 = Player(GREEN,[0,0])
    player2 = Player(BLUE,[0,0])
    running = True
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
                elif event.key == pygame.K_ESCAPE:
                    return None
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
        
    ## shows winner
    screen.fill(WHITE)
    win_text = "Winner is player " + str(winner)
    font1 = pygame.font.Font("freesansbold.ttf", 50)
    text = font1.render(win_text,True,BLACK)
    screen.blit(text,(200,300))
    pygame.display.flip()    
    t.sleep(1)
    return None
    

def gen_info():   ## generates queues with needed values
    times = Queue(5)
    rounds = Queue(5)
    for i in range(5):
        time = (5-i)*100
        times.enqueue(time)
        rounds.enqueue(str(i+1))
    return times, rounds


def computer_race(screen,mazetype, pathtype):
    lost = False
    times, rounds = gen_info()
    
    end = False
    screen = pygame.display.set_mode((swidth, sheight))  ## initialises screen
    for i in range(5):
        time = times.dequeue()    ## gets time,round
        roun = rounds.dequeue()
        if end == True:
            break
        if lost == False:
            screen.fill(WHITE)
            font1 = pygame.font.Font("freesansbold.ttf", 50)
            string = "Round " + roun
            text = font1.render(string,True,BLACK)
            screen.blit(text,(200,300))
            pygame.display.flip()
            
            if mazetype == "Wilsons":    ## generates maze
                maze = WilsonsMazeGen(30) 
            elif mazetype == "Backtracking":
                maze = backtracking_maze()
            t.sleep(1)
            end = find_end(maze)
            if pathtype == "DFS":          ## generates path
                enemy_moves = dfs(maze,[0,0],end)
            elif pathtype == "A*":
                enemy_moves = A_star(maze,[0,0],end)
            esteps = conv_to_moves(enemy_moves)
            player = Player(GREEN,[0,0])   ## initialises player, enemy
            enemy1 = Player(GRAY,[0,0])
            running = True
            won = False
            timer = pygame.time.Clock()
            ms = 0
            esteps.pop(-1)
            while running: 
                emove = 0
                ms += timer.get_time()  ## add time since last tick to ms
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
                            running = False
                            end = True
                if ms>time:   ## checks how many milliseconds since last call
                    try:
                        step = esteps[0]
                        enemy1.move(step[1],step[0],maze)
                        esteps.pop(0)
            
                        ms = 0  ## resets time between enemy moves
                    except:
                        lost = True
                        running = False
                timer.tick()  ## increases timer
                screen.fill(WHITE)     ## when finished
                draw_maze(screen, maze)  ## draws maze
                player.draw(screen)
                enemy1.draw(screen)
                if maze[player.y][player.x] == "2" and rounds == []:  ## checks if player has reached goal
                    screen.fill(WHITE)   ## win screen
                    font1 = pygame.font.Font("freesansbold.ttf", 50)
                    text = font1.render("You won :)",True,BLACK)
                    screen.blit(text,(200,300))
                    pygame.display.flip()
                    t.sleep(1)
                    won = True
                    running = False
                elif maze[player.y][player.x] == "2":
                    running = False
                if maze[enemy1.y][enemy1.x] == "2":  ## checks if enemy has reached goal
                    screen.fill(WHITE)   ## loss screen
                    font1 = pygame.font.Font("freesansbold.ttf", 50)
                    text = font1.render("You lost :(",True,BLACK)
                    screen.blit(text,(200,300))
                    pygame.display.flip()
                    t.sleep(1)
                    
                    
                pygame.display.flip()



    
def gamemode2(screen, mazetype, pathtype):
    run = True
    while run:
        screen.fill("light blue")   ## draws buttons
        buttona = Button("Race computer",[230,150],RED,ORANGE,BLACK)    
        buttona.hovering()
        buttona.draw(screen)
        buttonb = Button("2-Player Mode",[230,250],RED,ORANGE,BLACK)    
        buttonb.hovering()
        buttonb.draw(screen)
        bbutton = Button("Back", [230,550],RED,ORANGE,BLACK)     ## quit button
        bbutton.hovering()
        bbutton.draw(screen)
        pygame.display.flip()
        if buttona.check_clicked():    ## loads game modes when button clicked
            computer_race(screen, mazetype, pathtype)
        if buttonb.check_clicked():   
            two_player_mode(screen, mazetype)
    
    
        
   
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT or bbutton.check_clicked():  ## checks to close program
                run = False
    
        pygame.display.flip()