import pygame
import random


grid_width = 20
grid_height = 16
square_size = 32
line_color = (0,0,0)
window_width = grid_width * square_size
window_height = grid_height * square_size
screen = pygame.display.set_mode((640, 512))

#initial mole position
mole_x = 0
mole_y = 0
def draw_grid():
    for i in range(0, window_width + 1, square_size):
        pygame.draw.line(screen,line_color,(i, 0),(i, window_height))
    for i in range(0, window_height + 1, square_size):
        pygame.draw.line(
            screen,
            line_color,
            (0, i),
            (window_width, i)
        )
def add_mole(x,y):
    # You can draw the mole with this snippet:
    mole_image = pygame.image.load("mole.png")
    screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
def move_mole():
    rand_x = random.randrange(0, 20)
    rand_y = random.randrange(0, 16)
    return rand_x, rand_y

def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            screen.fill((218,177,218))
            draw_grid()
            add_mole(mole_x,mole_y)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = event.pos
                    width_pos = x // 32
                    height_pos = y // 32

                    # grid_x = x // square_size
                    # grid_y = y // square_size

                    if mole_x == width_pos and mole_y == height_pos:
                        x_mole, y_mole = move_mole()


            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

