def set_board():
    ''' function to create the game board '''
    return [[ "-" for _ in range(3)] for _ in range(3)]

def show_board(board):
    ''' function to show the game board '''
    for row in board:
        print(row[0] + " | " + row[1] + " | " + row[2])

def valid_play(board, row_move, col_move):
    ''' function to check if the play is valid or not '''
    if board[row_move][col_move] == "X" or board[row_move][col_move] == "O":
        return False
    
    if row_move >= 3 or col_move >= 3 or row_move < 0 or col_move < 0:
        return False
    
    return True

def check_winner(board, player_char, computer_char):
    ''' function to check winner '''

    # check row winning scenario
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "-":
            return row[0]
    
    # check column winning scenario
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "-":
            return board[0][col]
    
    # check diagonal winning scenario
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        return board[0][0]
    
    # check anti-diagonal winning scenario
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] != "-":
        return board[2][0]
    
    return None