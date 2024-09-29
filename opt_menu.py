import pygame
pygame.init()
font = pygame.font.Font("freesansbold.ttf", 24)
bfont = pygame.font.Font("freesansbold.ttf", 50)
#screen.fill("light blue")
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
    
    def draw(self,screen):
        if self.state == True:
            btn = pygame.draw.rect(screen, self.ocol, self.button,0,5)
            pygame.draw.rect(screen, self.mcol, self.button,5,5)
        elif self.state == False:
            btn = pygame.draw.rect(screen, self.mcol, self.button,0,5)
            pygame.draw.rect(screen, self.ocol, self.button,5,5)
        font = pygame.font.Font("freesansbold.ttf", 24)
        text = font.render(self.text,True,self.textcol)
        screen.blit(text,(self.pos[0]+15,self.pos[1]+7))
        
    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False
            
    def get_state(self):
        return self.state
    
    def change_state(self):
        if self.state == True:
            self.state = False
        else:
            self.state = True
            
def option_menu(screen):    
    run = True
    bfont = pygame.font.Font("freesansbold.ttf", 50)
    wilsons = optButton("Wilsons",[80,150],ORANGE,RED,BLACK,True)
    maze2 = optButton("Backtracking",[400,150],ORANGE,RED,BLACK,False)
    dfs = optButton("DFS",[80,400],ORANGE,RED,BLACK,True)
    path2 = optButton("Path 2",[400,400],ORANGE,RED,BLACK,False)
    back_button = optButton("BACK",[230,600],ORANGE,RED,BLACK,True)
    while run:
        screen.fill("light blue")     ## draw initial screen
        text = bfont.render("MAZE GENERATION",True,BLACK)
        screen.blit(text,(120,40))
        text1 = bfont.render("PATHFINDING",True,BLACK)
        screen.blit(text1,(200,300))
        wilsons.draw(screen)
        maze2.draw(screen)
        dfs.draw(screen)
        path2.draw(screen)
        back_button.draw(screen)
        if wilsons.check_clicked() or maze2.check_clicked():   ## check if buttons are clicked and change state as required
            wilsons.change_state()
            maze2.change_state()
            time.sleep(0.1)
        if dfs.check_clicked() or path2.check_clicked():
            dfs.change_state()
            path2.change_state()
            time.sleep(0.1)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or back_button.check_clicked(): ## go back to main menu and return chosen buttons
                if wilsons.get_state():
                    maze = "wilsons"
                else:
                    maze = "bactracking"
                if dfs.get_state():
                    pathfinding = "dfs"
                else:
                    pathfinding = "path2"
                    time.sleep(0.1)
                return [maze,pathfinding]
                    
        #time.sleep(1)
#screen = pygame.display.set_mode([720,720])
#print(option_menu(screen))
pygame.quit()