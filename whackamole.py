import pygame
import random


grid_width = 20
grid_height = 16
square_size = 32
line_color = (0,0,0)
window_width = grid_width * square_size
window_height = grid_height * square_size
screen = pygame.display.set_mode((640, 512))


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
def add_mole(mole_x,mole_y):
    # You can draw the mole with this snippet:
    mole_image = pygame.image.load("mole.png")
    screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
def move_mole():
    rand_x = random.randrange(0, grid_width) * square_size
    rand_y = random.randrange(0, grid_height) * square_size
    return rand_x, rand_y

def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        mole_x, mole_y = 0,0
        running = True
        while running:
            screen.fill((218, 177, 218))
            draw_grid()
            add_mole(mole_x, mole_y)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = event.pos
                    width_pos = y // 32
                    height_pos = x // 32


                    if width_pos == mole_y // 32 and height_pos == mole_x//32:
                        mole_x, mole_y = move_mole()



            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

