# Write your solution here
def column_correct(sudoku: list, column_no: int):
    column = [row[column_no] for row in sudoku]
    seen_numbers = []

    for num in column:
        if num != 0:
            if num in seen_numbers:
                return False
            seen_numbers.append(num)

    return True