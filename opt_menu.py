from distutils.archive_util import make_zipfile
from turtle import ondrag
import pygame
pygame.init()
screen = pygame.display.set_mode([720,720])
font = pygame.font.Font("freesansbold.ttf", 24)
screen.fill("light blue")
pygame.display.set_caption("Maze Game")
fps = 60
timer = pygame.time.Clock()
import time

WHITE = ((255,255,255))
BLUE = ((0,0,255))
GREEN = ((0,255,0))
RED = ((255,0,0))
BLACK = ((0,0,0))
ORANGE = ((255,100,10))
YELLOW = ((255,255,0))

class optButton:
    def __init__(self,txt,pos,mcol,ocol,textcol,state):
        self.text = txt
        self.pos = pos
        self.mcol = mcol
        self.ocol = ocol
        self.textcol = textcol
        self.button = pygame.rect.Rect((self.pos[0],self.pos[1]),(260,40))
        self.state = state
    
    def draw(self):
        if self.state == True:
            pygame.draw.rect(screen, self.ocol, self.button,0,5)
            pygame.draw.rect(screen, self.mcol, self.button,5,5)
        elif self.state == False:
            pygame.draw.rect(screen, self.mcol, self.button,0,5)
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
    def get_state(self):
        return self.state
    
    def change_state(self):
        if self.state == True:
            self.state = False
        else:
            self.state = True
            
def option_menu(screen):    
    run = True
    wilsons = optButton("Wilsons",[100,150],ORANGE,RED,BLACK,True)
    maze2 = optButton("maze2",[400,150],ORANGE,RED,BLACK,False)
    while run:
        screen.fill(WHITE)
        
        wilsons.draw()
        #wilsons.hovering()
        maze2.draw()
        #maze2.hovering()
        #print(wilsons.get_state())
        if wilsons.check_clicked() or maze2.check_clicked():
            wilsons.change_state()
            maze2.change_state()
            time.sleep(0.08)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                run = False
        #time.sleep(1)
        
option_menu(screen)
pygame.quit()