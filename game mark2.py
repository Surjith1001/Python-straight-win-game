import random

# initialize the board with 3 white and 3 black coins
board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]
white_coins = 3
black_coins = 3

# function to print the board
def print_board():
    print('  0 1 2')
    for i in range(3):
        print(i, end=' ')
        for j in range(3):
            print(board[i][j], end=' ')
        print()

# function to check if a move is valid
def is_valid_move(row, col):
    if row < 0 or row > 2 or col < 0 or col > 2:
        return False
    if board[row][col] != '-':
        return False
    return True

# function to check if there's a winner
def check_winner(player):
    symbol = 'W' if player == 1 else 'B'
    # check for horizontal wins
    for row in range(3):
        if board[row][0] == symbol and board[row][1] == symbol and board[row][2] == symbol:
            return True
    # check for vertical wins
    for col in range(3):
        if board[0][col] == symbol and board[1][col] == symbol and board[2][col] == symbol:
            return True
    return False

# function to get a valid move from a player
def get_move(player):
    while True:
        print('Player', player)
        row = int(input('Enter row: '))
        col = int(input('Enter col: '))
        if is_valid_move(row, col):
            return (row, col)
        else:
            print('Invalid move. Try again.')

# function to move a coin
def move_coin(player):
    symbol = 'W' if player == 1 else 'B'
    while True:
        print('Player', player, 'move a', symbol, 'coin.')
        row = int(input('Enter current row: '))
        col = int(input('Enter current col: '))
        if board[row][col] == symbol:
            while True:
                new_row = int(input('Enter new row: '))
                new_col = int(input('Enter new col: '))
                if is_valid_move(new_row, new_col):
                    board[row][col] = '-'
                    board[new_row][new_col] = symbol
                    return
                else:
                    print('Invalid move. Try again.')
        else:
            print('Invalid move. Try again.')

# main game loop
player = 1
while True:
    print_board()
    if player == 1:
        if white_coins > 0:
            # player 1 places a coin
            print('Player 1, place a white coin.')
            row, col = get_move(player)
            board[row][col] = 'W'
            white_coins -= 1
        else:
            # player 1 moves a coin
            move_coin(player)
    else:
        if black_coins > 0:
            # player 2 places a coin
            print('Player 2, place a black coin.')
            row, col = get_move(player)
            board[row][col] = 'B'
            black_coins -= 1
        else:
            # player 2 moves a coin
            move_coin(player)


    if check_winner(player):
        print_board()
        print('Player', player, 'wins!')
        break
    player = 1 if player == 2 else 2



