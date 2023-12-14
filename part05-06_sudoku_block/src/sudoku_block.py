# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    block = [
        sudoku[row_no][column_no:column_no + 3],
        sudoku[row_no + 1][column_no:column_no + 3],
        sudoku[row_no + 2][column_no:column_no + 3]
    ]
    seen_numbers = []
    for num in block:
        for n in num:
            if n != 0:
                if n in seen_numbers:
                    return False
                seen_numbers.append(n)
    return True


if __name__ == "__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))
