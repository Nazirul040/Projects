import numpy as np

def sudoku_solver(sudoku):

    def is_valid(sudoku, row, col, num):
        # Check if 'num' is not in the current row
        if num in sudoku[row]:
            return False
        
        # Check if 'num' is not in the current column
        if num in sudoku[:, col]:
            return False
        
        # Determine the starting point of the 3x3 subgrid
        start_row, start_col = row - row % 3, col - col % 3
        
        # Check if 'num' is not in the current 3x3 subgrid
        subgrid = sudoku[start_row:start_row + 3, start_col:start_col + 3]
        if num in subgrid:
            return False
        
        return True

    def solve_sudoku():
        for row in range(9):
            for col in range(9):
                if sudoku[row][col] == 0:  # Find an empty cell
                    for num in range(1, 10):  # Try numbers 1-9
                        if is_valid(sudoku, row, col, num):
                            sudoku[row][col] = num  # Place the number
                            
                            # Recursively try to solve the rest of the board
                            if solve_sudoku():
                                return True
                            
                            # If placing 'num' doesn't lead to a solution, reset the cell
                            sudoku[row][col] = 0
                    
                    # If no number can be placed, backtrack
                    return False
        
        # If all cells are filled correctly, the board is solved
        return True    
    
    if sudoku.shape != (9, 9):
        raise ValueError("Sudoku must be 9x9")
    
    if solve_sudoku():
        return sudoku
    else:
        raise ValueError("Can't be solved")


if __name__ == '__main__':
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    sudoku = np.array(sudoku_board)
    
    solved_sudoku = sudoku_solver(sudoku)
    if solved_sudoku is not None:
        print("Sudoku solved successfully!")
        for row in solved_sudoku:
            print(" ".join(str(num) for num in row))