import pygame as pg
from numpy.distutils.misc_util import blue_text

cell_size = 40
grid_size = 15
width = height = cell_size*grid_size

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0) #apples
orange = (255, 128, 0) #oranges
pink = (255, 0, 255) #R1 & R2
green = (0, 255, 0) #grass
brown = (0, 0, 128)

def draw_grid(screen, grid):
    screen.fill(green)
    font = pg.font.SysFont('None',20)

    for i in range(grid_size):
        for j in range(grid_size):
            rect = pg.Rect(i*cell_size, j*cell_size, cell_size, cell_size )
            cell = grid[i][j]

            if cell == '#':
                pg.draw.rect(screen, brown,rect)
            elif cell == "A":
                pg.draw.rect(screen,red,rect)
            elif cell == "O":
                pg.draw.rect(screen,orange,rect)
            elif cell == ".":
                pg.draw.rect(screen,green,rect)
            elif cell == "R1":
                pg.draw.rect(screen,pink,rect)
                text = font.render('1',True,white)
                screen.blit(text,(j*cell_size + 12, i*cell_size + 12))
            elif cell == "R2":
                pg.draw.rect(screen,pink,rect)
                text = font.render('2',True,white)
                screen.blit(text,(j*cell_size + 12, i*cell_size + 12))
            pg.draw.rect(screen,black,rect,1)

        pg.display.flip()

def start_pg():
    pg.init()
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("Autonomous Robot Farm Simulation")
    return screen

def actions():
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()
            exit()