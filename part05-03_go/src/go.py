# Write your solution here
def who_won(game_board: list):
    player1 = 0
    player2 = 0
    empty = 0

    for g in game_board:
        for b in g:
            if b == 1:
                player1 += 1
            elif b == 2:
                player2 += 1
            elif b == 0:
                empty += 1
            else:
                return "Something went wrong"
    
    if player1 > player2:
        return 1
    elif player1 < player2:
        return 2
    else:
        return 0


if __name__ == "__main__":
    board = [[1,2,1],[0,0,1],[2,1,0]]
    print(who_won(board))