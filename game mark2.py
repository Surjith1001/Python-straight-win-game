import tkinter as tk
from tkinter import messagebox

# Initialize the board with 3 white and 3 black coins
board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
white_coins = 3
black_coins = 3
placing_phase = True
selected_coin = None

# Function to print the board (for debugging purposes)
def print_board():
    for row in board:
        print(' '.join(row))
    print()

# Function to check if a move is valid
def is_valid_move(row, col):
    if row < 0 or row > 2 or col < 0 or col > 2:
        return False
    if board[row][col] != '-':
        return False
    return True

# Function to check if there's a winner
def check_winner(player):
    symbol = 'W' if player == 1 else 'B'
    # Check for horizontal wins
    for row in range(3):
        if board[row][0] == symbol and board[row][1] == symbol and board[row][2] == symbol:
            return True
    # Check for vertical wins
    for col in range(3):
        if board[0][col] == symbol and board[1][col] == symbol and board[2][col] == symbol:
            return True
    return False

# Function to handle a player's move
def handle_click(row, col):
    global player, white_coins, black_coins, placing_phase, selected_coin
    if placing_phase:
        if is_valid_move(row, col):
            if player == 1 and white_coins > 0:
                board[row][col] = 'W'
                white_coins -= 1
            elif player == 2 and black_coins > 0:
                board[row][col] = 'B'
                black_coins -= 1
            else:
                return  # Invalid move, do nothing
            update_board()
            if check_winner(player):
                messagebox.showinfo("Game Over", f"Player {player} wins!")
                reset_game()
            elif white_coins == 0 and black_coins == 0:
                placing_phase = False
            else:
                player = 1 if player == 2 else 2
                label.config(text=f"Player {player}'s turn")
    else:
        symbol = 'W' if player == 1 else 'B'
        if selected_coin is None and board[row][col] == symbol:
            selected_coin = (row, col)
            highlight_selected_coin(selected_coin)
        elif selected_coin:
            old_row, old_col = selected_coin
            if (row == old_row and abs(col - old_col) == 1) or (col == old_col and abs(row - old_row) == 1):
                if is_valid_move(row, col):
                    board[old_row][old_col] = '-'
                    board[row][col] = symbol
                    selected_coin = None
                    update_board()
                    if check_winner(player):
                        messagebox.showinfo("Game Over", f"Player {player} wins!")
                        reset_game()
                    else:
                        player = 1 if player == 2 else 2
                        label.config(text=f"Player {player}'s turn")
            else:
                selected_coin = None
                update_board()  # Remove highlights if move is invalid

def update_board():
    for row in range(3):
        for col in range(3):
            draw_coin(row, col)

def draw_coin(row, col):
    canvas = buttons[row][col]
    canvas.delete("all")
    if board[row][col] == 'W':
        canvas.create_oval(10, 10, 90, 90, fill="green")
    elif board[row][col] == 'B':
        canvas.create_oval(10, 10, 90, 90, fill="black")

def highlight_selected_coin(coin):
    row, col = coin
    buttons[row][col].create_rectangle(0, 0, 100, 100, outline="yellow", width=4)

def reset_game():
    global board, white_coins, black_coins, player, placing_phase, selected_coin
    board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    white_coins = 3
    black_coins = 3
    placing_phase = True
    selected_coin = None
    player = 1
    update_board()
    label.config(text="Player 1's turn")

# Create the main window
root = tk.Tk()
root.title("Simple Coin Game")

# Create a label to show the current player
player = 1
label = tk.Label(root, text="Player 1's turn", font=("Helvetica", 16))
label.grid(row=0, column=0, columnspan=3)

# Create the board buttons using Canvas to draw circles
buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        canvas = tk.Canvas(root, width=100, height=100, bg="white")
        canvas.grid(row=row+1, column=col)  # Adjusted row index to start from 1
        canvas.bind("<Button-1>", lambda event, r=row, c=col: handle_click(r, c))
        button_row.append(canvas)
    buttons.append(button_row)

# Create a reset button
reset_button = tk.Button(root, text="Reset Game", font=("Helvetica", 16), command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3)

# Start the main event loop
root.mainloop()
