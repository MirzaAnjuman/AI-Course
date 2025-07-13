# Chess Game Using Python

## How to Run
1. Make sure you have Python installed on your system.
2. Install the required libraries:
   ```
   pip install pygame python-chess
   ```
3. Run the game from the terminal:
   ```
   python chess.py
   ```

## Required Libraries
- Python 3.x
- pygame
- python-chess

## How to Play
- You play as White; the computer plays as Black.
- Click on a piece to select it. Legal moves will be highlighted.
- Click on a highlighted square to move your piece.
- The computer will automatically make its move after yours.
- The game follows standard chess rules, including pawn promotion and checkmate.
- The game ends when there is a checkmate, stalemate, or draw.

## Screenshot
![Game Screenshot](game_screenshot.png)

## Algorithm Used
- The computer AI uses the Minimax algorithm with Alpha-Beta pruning (depth-limited for performance) to select its moves.

