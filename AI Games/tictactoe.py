import tkinter as tk
from tkinter import messagebox
import math
import time
import threading

# Initialize board with 9 empty spaces
board = [' ' for _ in range(9)]

# To store button references for UI updates
buttons = []

# Player and Computer scores
player_score = 0
computer_score = 0

# Track which player starts first
player_first = True

# Track whose turn it is: 'X' for player, 'O' for computer
current_turn = 'X'

# Function to check if a player has won
def check_winner(b, player):
    combos = [
        [0,1,2],[3,4,5],[6,7,8],  # Rows
        [0,3,6],[1,4,7],[2,5,8],  # Columns
        [0,4,8],[2,4,6]           # Diagonals
    ]
    for combo in combos:
        if all(b[i] == player for i in combo):
            return True
    return False

# Check if the board is full (i.e., game is a draw)
def is_full(b):
    return ' ' not in b

# Minimax algorithm with Alpha-Beta pruning
def minimax(b, depth, alpha, beta, is_max):
    # Base cases: check win/draw
    if check_winner(b, 'O'):
        return 1     # AI wins
    if check_winner(b, 'X'):
        return -1    # Player wins
    if is_full(b):
        return 0     # Draw

    # AI's turn (maximize)
    if is_max:
        max_eval = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                eval = minimax(b, depth + 1, alpha, beta, False)
                b[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:  # Prune
                    break
        return max_eval

    # Player's turn (minimize)
    else:
        min_eval = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                eval = minimax(b, depth + 1, alpha, beta, True)
                b[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:  # Prune
                    break
        return min_eval

# AI makes a move based on Minimax
def computer_move():
    time.sleep(0.5)  # Delay to simulate thinking
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, -math.inf, math.inf, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i

    # Make the best move
    if move != -1:
        board[move] = 'O'
        buttons[move].config(text='O', state='disabled')
        check_game_over()

# Handle player click
def click(pos):
    global current_turn
    if board[pos] == ' ' and current_turn == 'X':
        board[pos] = 'X'
        buttons[pos].config(text='X', state='disabled')
        current_turn = 'O'
        check_game_over()
        if not is_full(board):
            threading.Thread(target=run_computer_turn).start()

# Threaded AI move to avoid UI freeze
def run_computer_turn():
    global current_turn
    computer_move()
    current_turn = 'X'

# Check for win/loss/draw after each move
def check_game_over():
    global player_score, computer_score
    if check_winner(board, 'X'):
        player_score += 1
        update_score()
        messagebox.showinfo("Game Over", "You win!")
        disable_board()
    elif check_winner(board, 'O'):
        computer_score += 1
        update_score()
        messagebox.showinfo("Game Over", "Computer wins!")
        disable_board()
    elif is_full(board):
        messagebox.showinfo("Game Over", "It's a draw!")
        disable_board()

# Disable all buttons after game over
def disable_board():
    for btn in buttons:
        btn.config(state='disabled')

# Reset the game board and alternate who starts first
def reset_game():
    global board, current_turn, player_first
    board = [' ' for _ in range(9)]
    for i in range(9):
        buttons[i].config(text=' ', state='normal')
    player_first = not player_first
    current_turn = 'X' if player_first else 'O'
    if current_turn == 'O':
        threading.Thread(target=run_computer_turn).start()

# Update score label in UI
def update_score():
    score_label.config(text=f"You: {player_score}   Computer: {computer_score}")

# === GUI SETUP ===

root = tk.Tk()
root.title("Tic-Tac-Toe with Smart AI")

# Frame to hold the 3x3 grid buttons
frame = tk.Frame(root)
frame.pack()

# Create 9 buttons and add to grid
for i in range(9):
    btn = tk.Button(frame, text=' ', font=('Helvetica', 24), width=5, height=2,
                    command=lambda i=i: click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Score display
score_label = tk.Label(root, text="You: 0   Computer: 0", font=('Helvetica', 14))
score_label.pack(pady=5)

# Reset button
reset_btn = tk.Button(root, text="New Game", font=('Helvetica', 12), command=reset_game)
reset_btn.pack(pady=5)

# Start initial game if computer goes first
if current_turn == 'O':
    threading.Thread(target=run_computer_turn).start()

# Run the GUI loop
root.mainloop()
