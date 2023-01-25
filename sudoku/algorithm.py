import numpy as np
import copy
import time

def algorithm_solve(sudoku_example):

    start_time = time.time()

    grid = np.array([[0]*9]*9)
    

    sudoku_example_grid = np.array(sudoku_example)

    def getSmallSquare(grid, row, col):
        square_number = (col // 3) + (row // 3)*3
        row_border = row // 3 * 3
        col_border = col // 3 * 3
        extracted_square = grid[row_border:row_border+3, col_border:col_border+3]

        return extracted_square

    def checkAvailiableVal(grid, row, col):
        if grid[row][col] != 0:
            print("Already a value in the cell")
            return None
        availiable = []
        for i in range(1, 10):
            if (i not in grid[row]) and (i not in grid[:, col]) and (i not in getSmallSquare(grid, row, col)):
                availiable.append(i)
        return availiable

    def recursive_solve(grid, row, col):

        while grid[row][col] != 0:
            if col == 8 and row == 8:
                return grid
            elif col == 8:
                row += 1
                col = 0
            else:
                col += 1
            
        availiable_values = checkAvailiableVal(grid, row, col)
        
        if len(availiable_values) == 0:
            return None
        
        is_succes = False
        for i in availiable_values:
            new_grid = copy.deepcopy(grid)
            new_grid[row][col] = i

            if col == 8 and row == 8:
                return new_grid
            elif col == 8:
                result = recursive_solve(new_grid, row + 1, 0)
            else: 
                result = recursive_solve(new_grid, row, col + 1)
                
            if result is None:
                continue
            else:
                is_succes = True
                break
        
        if is_succes:
            return result
        
        return None
            
    res = recursive_solve(sudoku_example_grid, 0, 0)

    return str("%s" % (time.time() - start_time))[:6] + " seconds"

