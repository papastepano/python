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