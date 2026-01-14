import random
import connect4 as c4

def make_random_move(board):
    valid_moves = c4.get_valid_moves(board)
    if not valid_moves:
        return None  # No valid moves available
    chosen_col = random.choice(valid_moves)
    
    return chosen_col

EMPTY = 0

def winning_moves(board, currPlayer):
    wins = []
    for col in c4.get_valid_moves(board):
        temp_board = [row[:] for row in board]
        c4.drop_piece(temp_board, col, currPlayer)
        if c4.has_winner(temp_board, currPlayer):
            wins.append(col)

    return wins

def evaluate_window(window, ai_piece, human_piece):
    score = 0

    if window.count(ai_piece) == 4:
        score += 100000
    elif window.count(ai_piece) == 3 and window.count(EMPTY) == 1:
        score += 100
    elif window.count(ai_piece) == 2 and window.count(EMPTY) == 2:
        score += 10

    if window.count(human_piece) == 3 and window.count(EMPTY) == 1:
        score -= 90
    elif window.count(human_piece) == 2 and window.count(EMPTY) == 2:
        score -= 5


    return score


def score_position(board):
    ai_piece = c4.P2
    human_piece = c4.P1
    ROWS, COLS = len(board), len(board[0])

    score = 0

    # Prefer centre column
    centre_col = COLS // 2
    centre_cells = [board[r][centre_col] for r in range(ROWS)]
    score += centre_cells.count(ai_piece) * 6

    # Horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            window = board[r][c:c+4]
            score += evaluate_window(window, ai_piece, human_piece)

    # Vertical
    for c in range(COLS):
        col_array = [board[r][c] for r in range(ROWS)]
        for r in range(ROWS - 3):
            window = col_array[r:r+4]
            score += evaluate_window(window, ai_piece, human_piece)

# Positive diagonal (/)
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            window = [board[r+i][c+i] for i in range(4)]
            score += evaluate_window(window, ai_piece, human_piece)

    # Negative diagonal (\)
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            window = [board[r-i][c+i] for i in range(4)]
            score += evaluate_window(window, ai_piece, human_piece)

    return score


#mininax algorithm for optimal move
def minimax(board, depth, alpha, beta, maximizingPlayer):
    best_order = [3, 4, 2, 5, 1, 6, 0]  # Prefer center columns
    valid_moves = c4.get_valid_moves(board)
    #order valid moves based on best_order
    valid_moves.sort(key=lambda x: best_order.index(x))
    
    

    is_terminal = c4.has_winner(board, c4.P1) or c4.has_winner(board, c4.P2) or c4.check_draw(board)
    
    if depth == 0 or is_terminal:
        if c4.has_winner(board, c4.P2):
            
            return (None, 10_000_000 + depth) 
        elif c4.has_winner(board, c4.P1):
            
            return (None, -10_000_000 - depth)
        
        elif c4.check_draw(board):
            return (None, 0)
        else:
            return (None, score_position(board))
    
    if maximizingPlayer:
        value = -float('inf')
        column = valid_moves[0]
        for col in valid_moves:
            temp_board = [row[:] for row in board]
            c4.drop_piece(temp_board, col, c4.P2)


            new_score = minimax(temp_board, depth-1, alpha, beta, False)[1]

            if new_score > value:
                value = new_score
                column = col
            
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value
    
    else:
        value = float('inf')
        column = valid_moves[0]
        for col in valid_moves:
            temp_board = [row[:] for row in board]
            c4.drop_piece(temp_board, col, c4.P1)

            new_score = minimax(temp_board, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break   
        return column, value
    
def make_optimal_move(board, depth):
    col, minimax_score = minimax(board, depth, -float('inf'), float('inf'), True)
    return col

