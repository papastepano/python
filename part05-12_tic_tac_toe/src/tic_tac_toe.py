# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):    
    if y in range(len(game_board)):
        if x in range(len(game_board[y])):
            if game_board[y][x] == "":
                game_board[y][x] = piece
                return True
    return False

if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 3, 0, "X"))
    print(game_board)

    #True
    #[['', '', 'X'], ['', '', ''], ['', '', '']]