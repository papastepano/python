# Write your solution here
def row_correct(sudoku: list, row_no: int):
    row = sudoku[row_no]
    seen_numbers = []

    for num in row:
        if num != 0:
            if num in seen_numbers:
                return False
            seen_numbers.append(num)

    return True

def column_correct(sudoku: list, column_no: int):
    column = [row[column_no] for row in sudoku]
    seen_numbers = []

    for num in column:
        if num != 0:
            if num in seen_numbers:
                return False
            seen_numbers.append(num)

    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    block = [
        sudoku[row_no][column_no:column_no + 3],
        sudoku[row_no + 1][column_no:column_no + 3],
        sudoku[row_no + 2][column_no:column_no + 3]
    ]
    seen_numbers = []

    for row in block:
        for n in row:
            if n != 0:
                if n in seen_numbers:
                    return False
                seen_numbers.append(n)

    return True

def sudoku_grid_correct(sudoku: list):
    for i in range(9):
        if not row_correct(sudoku, i) or not column_correct(sudoku, i):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not block_correct(sudoku, i, j):
                return False

    return True
