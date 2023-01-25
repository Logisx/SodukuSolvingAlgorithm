import pygame 
import pygame_widgets
from pygame_widgets import button
from sudoku.grid import Grid
from sudoku.solve import Solve
from sudoku.constants import BLACK, WHITE, HEIGHT, WIDTH, FONT

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sudoku solving algorithm')
pygame.font.init()


def option1():
    run = True
    clock = pygame.time.Clock()
    grid = Grid()
    solve = Solve()
    solve.start_pos(WIN)

    pygame.display.update()
    solve.start(WIN)
    while run:
        clock.tick(FPS)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


def main():
    clock = pygame.time.Clock()

    butn1 = button.Button(WIN, 76, HEIGHT // 2 - 60, WIDTH - 150, 100, text='Solve sudoku',
    fontSize=50, margin=20, round=10, 
    inactiveColour=(200, 30, 30), hoverColour = (200, 200, 200),
    onClick=lambda: option1()
    )

    run = True

    WIN.fill(BLACK)

    while run:
        clock.tick(FPS)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
        
        pygame_widgets.update(events)
        pygame.display.update()
        
    
    pygame.quit()




main()
