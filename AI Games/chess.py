import pygame
import sys
import os
import copy

pygame.init()

WIDTH, HEIGHT = 800, 640  
BOARD_WIDTH = 640
ROWS, COLS = 8, 8
SQUARE_SIZE = BOARD_WIDTH // COLS
SIDEBAR_WIDTH = WIDTH - BOARD_WIDTH

WHITE = (245, 245, 220)
BLACK = (139, 69, 19)
HIGHLIGHT = (255, 255, 0)
POSSIBLE_MOVE = (0, 255, 0)
CAPTURE_MOVE = (255, 0, 0)
SIDEBAR_BG = (240, 240, 240)
TEXT_COLOR = (50, 50, 50)

PIECE_VALUES = {
    'P': 1, 'p': -1,
    'N': 3, 'n': -3,
    'B': 3, 'b': -3,
    'R': 5, 'r': -5,
    'Q': 9, 'q': -9,
    'K': 1000, 'k': -1000
}


board = [
    list("rnbqkbnr"),
    list("pppppppp"),
    list("        "),
    list("        "),
    list("        "),
    list("        "),
    list("PPPPPPPP"),
    list("RNBQKBNR")
]


captured_white = []
captured_black = []


IMAGES = {}
image_folder = os.path.join(os.path.dirname(__file__), "images")
piece_to_file = {
    'P': 'Chess_plt60.png', 'p': 'Chess_pdt60.png',
    'R': 'Chess_rlt60.png', 'r': 'Chess_rdt60.png',
    'N': 'Chess_nlt60.png', 'n': 'Chess_ndt60.png',
    'B': 'Chess_blt60.png', 'b': 'Chess_bdt60.png',
    'Q': 'Chess_qlt60.png', 'q': 'Chess_qdt60.png',
    'K': 'Chess_klt60.png', 'k': 'Chess_kdt60.png',
}

for piece, filename in piece_to_file.items():
    path = os.path.join(image_folder, filename)
    try:
        image = pygame.image.load(path)
        IMAGES[piece] = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
    except pygame.error:
        
        surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
        color = (255, 255, 255) if piece.isupper() else (0, 0, 0)
        surface.fill(color)
        font = pygame.font.Font(None, 36)
        text = font.render(piece.upper(), True, (255, 0, 0) if piece.isupper() else (255, 255, 255))
        text_rect = text.get_rect(center=(SQUARE_SIZE//2, SQUARE_SIZE//2))
        surface.blit(text, text_rect)
        IMAGES[piece] = surface

def draw_board(win, selected_square, possible_moves):
    
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(win, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            
            
            if selected_square == (row, col):
                pygame.draw.rect(win, HIGHLIGHT, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 4)
    
    
    for move in possible_moves:
        (_, _), (to_row, to_col) = move
        
        is_capture = board[to_row][to_col] != ' '
        color = CAPTURE_MOVE if is_capture else POSSIBLE_MOVE
        
        center_x = to_col * SQUARE_SIZE + SQUARE_SIZE // 2
        center_y = to_row * SQUARE_SIZE + SQUARE_SIZE // 2
        
        if is_capture:
            
            pygame.draw.circle(win, color, (center_x, center_y), SQUARE_SIZE // 3, 4)
        else:
            
            pygame.draw.circle(win, color, (center_x, center_y), SQUARE_SIZE // 6)

def draw_pieces(win):
    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]
            if piece != ' ':
                win.blit(IMAGES[piece], (col * SQUARE_SIZE, row * SQUARE_SIZE))

def draw_sidebar(win, white_turn, game_status):
    
    pygame.draw.rect(win, SIDEBAR_BG, (BOARD_WIDTH, 0, SIDEBAR_WIDTH, HEIGHT))
    
    font = pygame.font.Font(None, 24)
    small_font = pygame.font.Font(None, 18)
    
    
    if game_status == "checkmate_white":
        status_text = "White Wins!"
        color = (0, 150, 0)
    elif game_status == "checkmate_black":
        status_text = "Black Wins!"
        color = (0, 150, 0)
    elif game_status == "stalemate":
        status_text = "Stalemate!"
        color = (150, 150, 0)
    elif game_status == "check_white":
        status_text = "White in Check"
        color = (200, 0, 0)
    elif game_status == "check_black":
        status_text = "Black in Check"
        color = (200, 0, 0)
    else:
        status_text = "White's Turn" if white_turn else "Black's Turn"
        color = TEXT_COLOR
    
    status_surface = font.render(status_text, True, color)
    win.blit(status_surface, (BOARD_WIDTH + 10, 10))
    
    
    title = small_font.render("Captured Pieces", True, TEXT_COLOR)
    win.blit(title, (BOARD_WIDTH + 10, 50))
    
    
    white_label = small_font.render("White pieces:", True, TEXT_COLOR)
    win.blit(white_label, (BOARD_WIDTH + 10, 80))
    
    y_offset = 100
    x_offset = BOARD_WIDTH + 10
    piece_size = 25
    pieces_per_row = 5
    
    for i, piece in enumerate(captured_white):
        row = i // pieces_per_row
        col = i % pieces_per_row
        x = x_offset + col * (piece_size + 3)
        y = y_offset + row * (piece_size + 3)
        
        
        scaled_piece = pygame.transform.scale(IMAGES[piece], (piece_size, piece_size))
        win.blit(scaled_piece, (x, y))
    
    
    black_y_start = y_offset + ((len(captured_white) // pieces_per_row + 1) * (piece_size + 3)) + 30
    black_label = small_font.render("Black pieces:", True, TEXT_COLOR)
    win.blit(black_label, (BOARD_WIDTH + 10, black_y_start))
    
    black_y_start += 20
    for i, piece in enumerate(captured_black):
        row = i // pieces_per_row
        col = i % pieces_per_row
        x = x_offset + col * (piece_size + 3)
        y = black_y_start + row * (piece_size + 3)
        
        
        scaled_piece = pygame.transform.scale(IMAGES[piece], (piece_size, piece_size))
        win.blit(scaled_piece, (x, y))
    
    
    white_material = sum(PIECE_VALUES.get(p, 0) for p in captured_black if p in PIECE_VALUES)
    black_material = sum(PIECE_VALUES.get(p, 0) for p in captured_white if p in PIECE_VALUES)
    material_diff = white_material - black_material
    
    advantage_y = HEIGHT - 100
    if material_diff > 0:
        advantage_text = f"White +{material_diff}"
    elif material_diff < 0:
        advantage_text = f"Black +{abs(material_diff)}"
    else:
        advantage_text = "Material equal"
    
    advantage_label = small_font.render("Material:", True, TEXT_COLOR)
    advantage_value = small_font.render(advantage_text, True, TEXT_COLOR)
    win.blit(advantage_label, (BOARD_WIDTH + 10, advantage_y))
    win.blit(advantage_value, (BOARD_WIDTH + 10, advantage_y + 20))
    
    
    if game_status in ["checkmate_white", "checkmate_black", "stalemate"]:
        restart_text = small_font.render("Press SPACE", True, TEXT_COLOR)
        restart_text2 = small_font.render("to restart", True, TEXT_COLOR)
        win.blit(restart_text, (BOARD_WIDTH + 10, HEIGHT - 50))
        win.blit(restart_text2, (BOARD_WIDTH + 10, HEIGHT - 30))

def is_valid_position(row, col):
    return 0 <= row < 8 and 0 <= col < 8

def get_piece_moves(board, r, c):
    piece = board[r][c]
    if piece == ' ':
        return []
    
    moves = []

    if piece.upper() == 'P':
        
        direction = -1 if piece.isupper() else 1
        start_row = 6 if piece.isupper() else 1
        
        
        new_row = r + direction
        if is_valid_position(new_row, c) and board[new_row][c] == ' ':
            moves.append(((r, c), (new_row, c)))
            
            
            if r == start_row and board[new_row + direction][c] == ' ':
                moves.append(((r, c), (new_row + direction, c)))
        
        
        for dc in [-1, 1]:
            new_row, new_col = r + direction, c + dc
            if is_valid_position(new_row, new_col):
                target = board[new_row][new_col]
                if target != ' ' and piece.isupper() != target.isupper():
                    moves.append(((r, c), (new_row, new_col)))
    
    elif piece.upper() == 'N':
        
        knight_moves = [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)]
        for dr, dc in knight_moves:
            new_row, new_col = r + dr, c + dc
            if is_valid_position(new_row, new_col):
                target = board[new_row][new_col]
                if target == ' ' or piece.isupper() != target.isupper():
                    moves.append(((r, c), (new_row, new_col)))
    
    elif piece.upper() in ['R', 'B', 'Q']:
        
        directions = []
        if piece.upper() == 'R':
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
        elif piece.upper() == 'B':
            directions = [(-1,-1), (-1,1), (1,-1), (1,1)]
        elif piece.upper() == 'Q':
            directions = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]
        
        for dr, dc in directions:
            for i in range(1, 8):
                new_row, new_col = r + dr * i, c + dc * i
                if not is_valid_position(new_row, new_col):
                    break
                    
                target = board[new_row][new_col]
                if target == ' ':
                    moves.append(((r, c), (new_row, new_col)))
                elif piece.isupper() != target.isupper():
                    moves.append(((r, c), (new_row, new_col)))
                    break
                else:
                    break
    
    elif piece.upper() == 'K':
        
        directions = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]
        for dr, dc in directions:
            new_row, new_col = r + dr, c + dc
            if is_valid_position(new_row, new_col):
                target = board[new_row][new_col]
                if target == ' ' or piece.isupper() != target.isupper():
                    moves.append(((r, c), (new_row, new_col)))

    return moves

def get_all_moves(board, white=True):
    """Get all possible moves for the given color (without checking for check)"""
    moves = []
    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece == ' ':
                continue
            if white and piece.isupper():
                moves.extend(get_piece_moves(board, r, c))
            elif not white and piece.islower():
                moves.extend(get_piece_moves(board, r, c))
    return moves

def find_king(board, white=True):
    """Find the position of the king for the given color"""
    king = 'K' if white else 'k'
    for r in range(8):
        for c in range(8):
            if board[r][c] == king:
                return (r, c)
    return None

def is_square_attacked(board, row, col, by_white=True):
    """Check if a square is attacked by the given color"""
    
    attacking_moves = get_all_moves(board, white=by_white)
    
    
    for move in attacking_moves:
        (_, _), (target_row, target_col) = move
        if target_row == row and target_col == col:
            return True
    return False

def is_in_check(board, white=True):
    """Check if the king of the given color is in check"""
    king_pos = find_king(board, white)
    if king_pos is None:
        return False
    
    king_row, king_col = king_pos
    return is_square_attacked(board, king_row, king_col, by_white=not white)

def is_legal_move(board, move):
    """Check if a move is legal (doesn't put own king in check)"""
    (from_row, from_col), (to_row, to_col) = move
    piece = board[from_row][from_col]
    
    if piece == ' ':
        return False
    
    
    temp_board = copy.deepcopy(board)
    temp_board[to_row][to_col] = temp_board[from_row][from_col]
    temp_board[from_row][from_col] = ' '
    
    
    white_piece = piece.isupper()
    return not is_in_check(temp_board, white=white_piece)

def get_legal_moves(board, white=True):
    """Get all legal moves for the given color (excluding moves that put king in check)"""
    all_moves = get_all_moves(board, white)
    legal_moves = []
    
    for move in all_moves:
        if is_legal_move(board, move):
            legal_moves.append(move)
    
    return legal_moves

def is_checkmate(board, white=True):
    """Check if the given color is in checkmate"""
    if not is_in_check(board, white):
        return False
    
    
    legal_moves = get_legal_moves(board, white)
    return len(legal_moves) == 0

def is_stalemate(board, white=True):
    """Check if the given color is in stalemate"""
    if is_in_check(board, white):
        return False
    
    
    legal_moves = get_legal_moves(board, white)
    return len(legal_moves) == 0

def get_game_status(board, white_turn):
    """Get the current game status"""
    if white_turn:
        if is_checkmate(board, white=True):
            return "checkmate_black"  
        elif is_stalemate(board, white=True):
            return "stalemate"
        elif is_in_check(board, white=True):
            return "check_white"
    else:
        if is_checkmate(board, white=False):
            return "checkmate_white"  
        elif is_stalemate(board, white=False):
            return "stalemate"
        elif is_in_check(board, white=False):
            return "check_black"
    
    return "playing"

def make_move(board, move):
    new_board = copy.deepcopy(board)
    (r1, c1), (r2, c2) = move
    
    
    captured_piece = new_board[r2][c2]
    
    
    new_board[r2][c2] = new_board[r1][c1]
    new_board[r1][c1] = ' '
    
    return new_board, captured_piece

def evaluate(board):
    score = 0
    for row in board:
        for piece in row:
            if piece in PIECE_VALUES:
                score += PIECE_VALUES[piece]
    return score

def minimax_legal(board, depth, maximizing):
    """Minimax that only considers legal moves"""
    if depth == 0:
        return evaluate(board), None
    
    moves = get_legal_moves(board, white=maximizing)
    if not moves:
        
        if is_in_check(board, white=maximizing):
            
            return -10000 if maximizing else 10000, None
        else:
            
            return 0, None
    
    best_move = None
    
    if maximizing:
        max_eval = -float('inf')
        for move in moves:
            new_board, _ = make_move(board, move)
            eval_score, _ = minimax_legal(new_board, depth - 1, False)
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in moves:
            new_board, _ = make_move(board, move)
            eval_score, _ = minimax_legal(new_board, depth - 1, True)
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move
        return min_eval, best_move

def main():
    global board, captured_white, captured_black
    
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Enhanced Chess Game")
    clock = pygame.time.Clock()
    
    selected = None
    possible_moves = []
    white_turn = True
    ai_thinking = False
    game_over = False

    running = True
    while running:
        clock.tick(30)
        
        
        game_status = get_game_status(board, white_turn)
        if game_status in ["checkmate_white", "checkmate_black", "stalemate"]:
            game_over = True
        
        
        draw_board(win, selected, possible_moves)
        draw_pieces(win)
        draw_sidebar(win, white_turn, game_status)
        pygame.display.flip()

        
        if not white_turn and not ai_thinking and not game_over:
            ai_thinking = True
            legal_moves = get_legal_moves(board, white=False)
            
            if legal_moves:
                
                _, ai_move = minimax_legal(board, 2, False)
                if ai_move and ai_move in legal_moves:
                    new_board, captured_piece = make_move(board, ai_move)
                    board = new_board
                    
                    
                    if captured_piece != ' ':
                        if captured_piece.isupper():
                            captured_white.append(captured_piece)
                        else:
                            captured_black.append(captured_piece)
            
            white_turn = True
            ai_thinking = False
            selected = None
            possible_moves = []

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and white_turn and not ai_thinking and not game_over:
                x, y = pygame.mouse.get_pos()
                
                
                if x >= BOARD_WIDTH:
                    continue
                    
                row, col = y // SQUARE_SIZE, x // SQUARE_SIZE
                
                if selected:
                    move = (selected, (row, col))
                    
                    if move in possible_moves:
                        
                        new_board, captured_piece = make_move(board, move)
                        board = new_board
                        
                        
                        if captured_piece != ' ':
                            if captured_piece.isupper():
                                captured_white.append(captured_piece)
                            else:
                                captured_black.append(captured_piece)
                        
                        
                        white_turn = False
                        selected = None
                        possible_moves = []
                    else:
                        
                        piece = board[row][col]
                        if piece != ' ' and piece.isupper():
                            selected = (row, col)
                            
                            piece_moves = get_piece_moves(board, row, col)
                            possible_moves = [move for move in piece_moves if is_legal_move(board, move)]
                        else:
                            selected = None
                            possible_moves = []
                else:
                    
                    piece = board[row][col]
                    if piece != ' ' and piece.isupper():
                        selected = (row, col)
                        
                        piece_moves = get_piece_moves(board, row, col)
                        possible_moves = [move for move in piece_moves if is_legal_move(board, move)]
            elif event.type == pygame.KEYDOWN and game_over:
                
                if event.key == pygame.K_SPACE:
                    
                    board = [
                        list("rnbqkbnr"),
                        list("pppppppp"),
                        list("        "),
                        list("        "),
                        list("        "),
                        list("        "),
                        list("PPPPPPPP"),
                        list("RNBQKBNR")
                    ]
                    captured_white = []
                    captured_black = []
                    selected = None
                    possible_moves = []
                    white_turn = True
                    game_over = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
