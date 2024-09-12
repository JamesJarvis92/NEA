##display menu with options for game mode
## run game modes
    ## select maze gen/solve algorithms etc
    ## play game 
    ## once completed show score/add to leaderboard
    ## go back to menu
## option to play another game or quit

from Gamemode1 import *
from Gamemode2 import *
from Gamemode3 import *

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



run = True
while run:
    screen.fill("light blue")
    timer.tick(fps)
    button1 = Button("Normal Mode",[300,100],RED,ORANGE,BLACK)    ## G1     ### add buttons to array so code is pretty
    button1.hovering()
    button1.draw()
    button2 = Button("2-Player Mode",[300,200],RED,ORANGE,BLACK)    ## G2
    button2.hovering()
    button2.draw()
    button3 = Button("Dark Mode",[300,300],RED,ORANGE,BLACK)    ## G3
    button3.hovering()
    button3.draw()
    qbutton = Button("QUIT", [300,500],RED,ORANGE,BLACK)     ## quit button
    qbutton.hovering()
    qbutton.draw()
    
    pygame.display.flip()
    if button1.check_clicked():   ### add time to complete (make maze with missing corner to have timer) and leaderboard,   countdown to start using while loop and sleep(1)
        gamemode1(screen)
    if button2.check_clicked():   ### add winner screen
        gamemode2(screen)
    if button3.check_clicked():
        gamemode3(screen)
        
   
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or qbutton.check_clicked():  ## checks to close program
            run = False
    
    pygame.display.flip()

pygame.quit()



## use pixel art to make maze look better
## make a function so i can draw images for each cell in square by working out which sides of each cell are walls
## potentially two images for character one walking, one stationary