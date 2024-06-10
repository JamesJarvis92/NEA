import pygame



pygame.init()
swidth = 720
sheight = 720   ## change cell size based on size of mazes
square_size = 80
MAZE_WIDTH = swidth // square_size
MAZE_HEIGHT = sheight // square_size 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (192, 192, 192)

def draw_maze(screen, maze):
    for y in range(MAZE_HEIGHT):
        for x in range(MAZE_WIDTH):
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
        if 0 <= new_x < MAZE_WIDTH and 0 <= new_y < MAZE_HEIGHT and maze[new_y][new_x] != "1":  ## checks square trying to move to is valid
            self.x = new_x    ## assigns new position
            self.y = new_y
    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, (self.x * square_size, self.y * square_size, square_size, square_size))  ##  draws player
        

def main():
    screen = pygame.display.set_mode((swidth, sheight))  ## initialises screen
    maze = ["001010001",
        "100011010",
        "101011011",
        "100000000",
        "101010101",
        "111010101",
        "101010100",
        "101010001",
        "000011211"]
    player = Player()
    running = True
    won = False
    while running:
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
        screen.fill(WHITE)
        draw_maze(screen, maze)  ## draws maze
        player.draw(screen)
        if maze[player.y][player.x] == "2":  ## checks if player has reached goal
            won = True
            running = False
        pygame.display.flip()
    screen.fill(WHITE)
    
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
if __name__ == "__main__":
    main()