def play_turn (game_board : list, x : int, y : int, symbol : str) -> bool :
    if game_board[x][y] == "" :
        game_board[x][y] = symbol
        return True
    
    return False
    


if __name__ == "__main__" :
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)