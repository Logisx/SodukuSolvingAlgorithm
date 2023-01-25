import numpy as np
import copy
import sys
import time
import pygame
from .grid import Grid
from .sugoku_examples import get_sudoku_example
from .constants import WIDTH, HEIGHT
from .algorithm import algorithm_solve

class Solve():

    def __init__(self):
        self.screen_grid = Grid()
        self.grid = np.array([[0]*9]*9)
        self.sudoku_example = get_sudoku_example()
        self.sudoku_example_grid = np.array(self.sudoku_example)
        self.delay = 0
        self.delayed = 0

    def start_pos(self, win):
        time_without_GUI = algorithm_solve(self.sudoku_example)
        self.start_time = time.time()
        self.info = [time_without_GUI, self.start_time]
        self.screen_grid.draw(win, self.sudoku_example, self.info)


    def start(self, win):
        self.win = win
        self.recursive_solve(self.sudoku_example_grid, 0, 0)

    def end_program(self):
        pygame.quit()
        sys.exit(0)

    def get_cur_time(self):
        return str("%s" % (time.time() - self.start_time - self.delayed))[:5] + " seconds"


    def getSmallSquare(self, grid, row, col):
        square_number = (col // 3) + (row // 3)*3
        row_border = row // 3 * 3
        col_border = col // 3 * 3
        extracted_square = grid[row_border:row_border+3, col_border:col_border+3]

        return extracted_square


    def checkAvailiableVal(self, grid, row, col):
        if grid[row][col] != 0:
            return None
        availiable = []
        for i in range(1, 10):
            if (i not in grid[row]) and (i not in grid[:, col]) and (i not in self.getSmallSquare(grid, row, col)):
                availiable.append(i)
        return availiable

    def slower(self):
        self.delay += 0.05

    def show_cur_result(self, cur_grid):
        self.info[1] = self.get_cur_time()
        self.screen_grid.draw(self.win, cur_grid, self.info)
        time.sleep(self.delay)
        self.delayed += self.delay
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.end_program()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()

                if ((WIDTH - 100) <= mouse[0] <= (WIDTH - 10)) and ((HEIGHT - 75) <= mouse[1] <= (HEIGHT - 25)):
                    self.slower()
        
        pygame.display.update()       



    def recursive_solve(self, grid, row, col):

        while grid[row][col] != 0:
            if col == 8 and row == 8:
                return grid
            elif col == 8:
                row += 1
                col = 0
            else:
                col += 1
            
        availiable_values = self.checkAvailiableVal(grid, row, col)
        
        if len(availiable_values) == 0:
            return None
        
        is_succes = False
        for i in availiable_values:
            new_grid = copy.deepcopy(grid)
            new_grid[row][col] = i


            self.show_cur_result(new_grid)

            if col == 8 and row == 8:
                return new_grid
            elif col == 8:
                result = self.recursive_solve(new_grid, row + 1, 0)
            else: 
                result = self.recursive_solve(new_grid, row, col + 1)
                
            if result is None:
                continue
            else:
                is_succes = True
                break
        
        if is_succes:
            return result
        
        self.show_cur_result(new_grid)
        self.screen_grid.show_wrong_cell(self.win, row, col)
        pygame.display.update()
        return None
    



