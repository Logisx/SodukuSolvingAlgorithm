import pygame
from .constants import WHITE, GREY, BLACK, FONT, CELL_SIZE, FONT_SIZE, HEIGHT, WIDTH, RED


class Grid():

    def __init__(self):
        pass

    def draw_grid(self, win):
        win.fill(BLACK)
        for row in range(0, 9):
            for col in range(0, 9):
                pygame.draw.rect(win, WHITE, (row * CELL_SIZE, col * CELL_SIZE, CELL_SIZE*0.98, CELL_SIZE*0.98))

    def draw_main_squares(self, win):
        pygame.draw.line(win, BLACK, (CELL_SIZE*3, 0), (CELL_SIZE*3, HEIGHT), 3)
        pygame.draw.line(win, BLACK, (CELL_SIZE*6, 0), (CELL_SIZE*6, HEIGHT), 3)
        pygame.draw.line(win, BLACK, (0, CELL_SIZE*3), (WIDTH, CELL_SIZE*3), 3)
        pygame.draw.line(win, BLACK, (0, CELL_SIZE*6), (WIDTH, CELL_SIZE*6), 3)

    def draw_info(self, win, info):
        pygame.draw.rect(win, GREY, (4, HEIGHT - 96, WIDTH - 8, 92))
        time_without_GUI, cur_time = str(info[0]), str(info[1])
        my_font1 = pygame.font.SysFont(FONT, 20)
        text_surface1 = my_font1.render('Time:  ' + cur_time, False, WHITE)
        win.blit(text_surface1, (20, HEIGHT - 75))

        my_font2 = pygame.font.SysFont(FONT, 20)
        text_surface2 = my_font2.render('Time without GUI:  ' + time_without_GUI, False, WHITE)
        win.blit(text_surface2, (20, HEIGHT - 50))

    def draw_slow_button(self, win):
        pygame.draw.rect(win, (200, 30, 30), (WIDTH - 100, HEIGHT - 75, 90, 50), 0, 5)
        my_font = pygame.font.SysFont(FONT, 18)
        text_surface = my_font.render('Slower', False, WHITE)
        win.blit(text_surface, (WIDTH - 80, HEIGHT - 60))


    def draw(self, win, sudoku_digits, info):

        self.draw_grid(win)
        self.draw_main_squares(win)
        self.draw_info(win, info)
        self.draw_slow_button(win)

        my_font = pygame.font.SysFont(FONT, FONT_SIZE)
        for row in range(0, 9):
            for col in range(0, 9):
                if sudoku_digits[row][col] != 0:
                    text_width, text_height = my_font.size(str(sudoku_digits[row][col]))
                    text_surface = my_font.render(str(sudoku_digits[row][col]), False, BLACK)
                    win.blit(text_surface, (col * CELL_SIZE + CELL_SIZE // 2 - text_width // 2, row * CELL_SIZE + CELL_SIZE // 2 - text_height // 2))
        

    def show_wrong_cell(self, win, row, col):
        pygame.draw.line(win, RED, (col * CELL_SIZE, row * CELL_SIZE), (col * CELL_SIZE + CELL_SIZE, row * CELL_SIZE), 3)
        pygame.draw.line(win, RED, (col * CELL_SIZE + CELL_SIZE, row * CELL_SIZE), (col * CELL_SIZE + CELL_SIZE, row * CELL_SIZE + CELL_SIZE), 3)
        pygame.draw.line(win, RED, (col * CELL_SIZE + CELL_SIZE, row * CELL_SIZE + CELL_SIZE), (col * CELL_SIZE, row * CELL_SIZE + CELL_SIZE), 3)
        pygame.draw.line(win, RED, (col * CELL_SIZE, row * CELL_SIZE + CELL_SIZE), (col * CELL_SIZE, row * CELL_SIZE), 3)
        

