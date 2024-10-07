
## use queue to hold round numbers, time etc.
## make new pathfinding
## make new maze

### add timer to g1
### sort crash when running second time
### add buttons passed into optmenu - dont reset everytime
 


from Gamemode1 import *
from Gamemode2 import *
from Gamemode3 import *
from Gamemode4 import *
from opt_menu import *
WHITE = ((255,255,255))
BLUE = ((0,0,255))
GREEN = ((0,255,0))
RED = ((255,0,0))
BLACK = ((0,0,0))
ORANGE = ((255,100,10))
YELLOW = ((255,255,0))

class Button:
    def __init__(self,txt,pos,mcol,ocol,textcol):
        self.text = txt
        self.pos = pos
        self.mcol = mcol
        self.ocol = ocol
        self.textcol = textcol
        self.button = pygame.rect.Rect((self.pos[0],self.pos[1]),(260,40))
    
    def draw(self):
        btn = pygame.draw.rect(screen, self.mcol, self.button,0,5)
        pygame.draw.rect(screen, self.ocol, self.button,5,5)
        text = font.render(self.text,True,self.textcol)
        screen.blit(text,(self.pos[0]+15,self.pos[1]+7))
        
    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False
        
    def hovering(self):
        if (self.button).collidepoint(pygame.mouse.get_pos()):
            temp = self.mcol
            self.mcol = self.ocol
            self.ocol = temp
        
        

import pygame
pygame.init()
WIDTH = 720
HEIGHT = 720
screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("Maze Game")
fps = 60
timer = pygame.time.Clock()
main_menu = True
font = pygame.font.Font("freesansbold.ttf", 24)
font1 = pygame.font.Font("freesansbold.ttf", 40)


var = ["Wilsons","DFS"]
run = True
while run:
    print(var)
    screen.fill("light blue")
    timer.tick(fps)
    text = font1.render("MAZE ESCAPE",True,BLACK)
    screen.blit(text,(210,40))
    button1 = Button("Normal Mode",[230,100],RED,ORANGE,BLACK)    ## G1     ### add buttons to array so code is pretty
    button1.hovering()
    button1.draw()
    button2 = Button("Race mode",[230,200],RED,ORANGE,BLACK)    ## G2
    button2.hovering()
    button2.draw()
    button3 = Button("Dark Mode",[230,300],RED,ORANGE,BLACK)    ## G3
    button3.hovering()
    button3.draw()
    button4 = Button("Escape enemies",[230,400],RED,ORANGE,BLACK)    ## G3
    button4.hovering()
    button4.draw()
    optbutton = Button("Options",[230,500],RED,ORANGE,BLACK)
    optbutton.hovering()
    optbutton.draw()
    qbutton = Button("QUIT", [230,600],RED,ORANGE,BLACK)     ## quit button
    qbutton.hovering()
    qbutton.draw()
    
    pygame.display.flip()
    if button1.check_clicked():   ### add time to complete (make maze with missing corner to have timer) and leaderboard,   countdown to start using while loop and sleep(1)
        gamemode1(screen,var[0])
    if button2.check_clicked():   
        gamemode2(screen,var[0],var[1])
    if button3.check_clicked():
        gamemode3(screen, var[0])
    if button4.check_clicked():
        gamemode4(screen)
    if optbutton.check_clicked():
        var = option_menu(screen)   ## [maze,path]
        print(var)
   
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or qbutton.check_clicked():  ## checks to close program
            run = False
    
    pygame.display.flip()

#pygame.quit()



