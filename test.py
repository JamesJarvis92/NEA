import pygame
pygame.init()
swidth = 720
sheight = 720   ## change cell size based on size of mazes
square_size = 80 ## need to calculate this based on maze size or just have set sizes for game modes
mwidth = swidth // square_size  -1
mheight = sheight // square_size  -1
print(mwidth,mheight)
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
                

maze = ["01000111",
        "01011100",
        "01110101",
        "11000101",
        "10000111"
        "11111100",
        "00010001",
        "00210001",
        "00011111"]

screen = pygame.display.set_mode([721,721])
screen.fill(WHITE)
while True:
    draw_maze(screen,maze)
    pygame.display.flip()