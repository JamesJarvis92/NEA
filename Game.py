##display menu with options for game mode
## run game modes
    ## select maze gen/solve algorithms etc
    ## play game 
    ## once completed show score/add to leaderboard
    ## go back to menu
## option to play another game or quit

from drawmaze import *


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

def draw_menu():
    button = Button("Normal Mode",[300,100],RED,ORANGE,BLACK)
    button.hovering()
    button.draw()
    return button.check_clicked()
"""
def draw_game():
    button = Button("menu",[350,350],RED,ORANGE,BLACK)
    button.draw()
    button.hovering()
    button.draw()
    return button.check_clicked()
"""
run = True
while run:
    screen.fill("light blue")
    timer.tick(fps)
    button = Button("Normal Mode",[300,100],RED,ORANGE,BLACK)
    button.hovering()
    button.draw()
    pygame.display.flip()
    if button.check_clicked():
        gamemode1(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()

pygame.quit()



## use pixel art to make maze look better
## make a function so i can draw images for each cell in square by working out which sides of each cell are walls
## potentially two images for character one walking, one stationary