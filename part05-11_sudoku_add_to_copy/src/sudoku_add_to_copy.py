# Write your solution here
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) -> list:
    copy = []
    for row in sudoku:
        new_row = []
        for value in row:
            new_row.append(value)
        copy.append(new_row)
    add_number(copy, row_no, column_no, number)
    return copy

def print_sudoku(sudoku: list):
    i = 1
    while i <= len(sudoku):
        for j in range(0, len(sudoku[i - 1]), 3):
            print(''.join('_ ' if value == 0 else f'{value} ' for value in sudoku[i - 1][j:j + 3]), end=' ')
        print()
        
        if i % 3 == 0:
            print()
        
        i += 1

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 1, 1, 5)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)