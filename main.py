# this is the "terminal" version of the game
# game version 1

import random
import base_funcs

def player_move(board, row_move, col_move, player_char):
    if base_funcs.valid_play(board, row_move, col_move):
        board[row_move][col_move] = player_char
    else:
        print("Invalid move. You lost your turn.\n")

def computer_move(board, computer_char):
    row_move = random.randint(0,2)
    col_move = random.randint(0,2)

    if base_funcs.valid_play(board, row_move, col_move):
        board[row_move][col_move] = computer_char
    else:
        print("Invalid move. The computer lost its turn.\n")

def main():
    ''' main function to play the game '''
    player_char = input("choose between X or O\n")
    player_char = player_char.upper()
    
    while player_char != "X" and player_char != "O":
        player_char = input("You didn't choose a valid option, please choose between X or O\n")
        player_char = player_char.upper()

    if player_char == "X":
        computer_char = "O"
    else:
        computer_char = "X"

    board = base_funcs.set_board()
    base_funcs.show_board(board)
    print()

    turn = random.choice(["computer", "player"])

    while True:
        if turn == "player":
            row_player_move = int(input("Choose in which row you want to play\n")) - 1
            col_player_move = int(input("Choose in which column you want to play\n")) - 1

            player_move(board, row_player_move, col_player_move, player_char)
            base_funcs.show_board(board)
            turn = "computer"

        else:
            computer_move(board, computer_char)
            base_funcs.show_board(board)
            turn = "player"

        print()

        winner = base_funcs.check_winner(board, player_char, computer_char)

        if winner:
            if winner == player_char:
                print(f"{player_char} is the winner!")
            else:
                print(f"{computer_char} is the winner!")
            break

if __name__ == "__main__":
    main()