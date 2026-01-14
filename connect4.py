import pygame


CARD_W, CARD_H = 260, 180
CARD_GAP = 40


WIDTH, HEIGHT = 700, 600


BOTS = [
    {"id": "easy",   "name": "Easy Bot",   "subtitle": "No brain", "depth": 1},
    {"id": "medium", "name": "Medium Bot", "subtitle": "Decent", "depth": 4},
    {"id": "hard",   "name": "Hard Bot",   "subtitle": "Can see the future", "depth": 6},
]

selected_bot = None
bot_depth = None

menu_cards = [] 
total_w = 3 * CARD_W + 2 * CARD_GAP
start_x = (WIDTH - total_w) // 2
y = HEIGHT // 2 - CARD_H // 2 #just works idk

def build_menu_cards(WIDTH, HEIGHT, bots):
    
    margin_x = max(16, WIDTH // 30)      # ~23 at 700
    gap = max(14, WIDTH // 35)           # ~20 at 700

    card_w = (WIDTH - 2 * margin_x - 2 * gap) // 3
    card_h = min(190, int(HEIGHT * 0.30))  # lowk googled this ratio

    y = int(HEIGHT * 0.38)               # places cards under title

    cards = []
    x = margin_x
    for bot in bots:
        rect = pygame.Rect(x, y, card_w, card_h)
        cards.append((rect, bot))
        x += card_w + gap

    return cards

menu_cards = build_menu_cards(WIDTH, HEIGHT, BOTS)

EMPTY = 0
P1 = 1
P2 = 2
ROWS = 5
COLS = 7

#function to get all valid moves
def get_valid_moves(board):
    return [c for c in range(COLS) if board[0][c] == EMPTY]

#function to drop a piece in the board
def drop_piece(board, col, currPlayer):
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == EMPTY:
            board[r][col] = currPlayer
            return (r, col)
    return None

#function to draw the bot selection menu
def draw_bot_menu(screen):
    screen.fill((0, 0, 30))

    title_font = pygame.font.SysFont(None, 74)
    card_title_font = pygame.font.SysFont(None, 40)
    card_sub_font = pygame.font.SysFont(None, 26)

    title_text = title_font.render("Connect Four", True, (200, 200, 200))
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 8)) #centered at top

    mx, my = pygame.mouse.get_pos()

    for rect, bot in menu_cards:
        hovered = rect.collidepoint(mx, my)

        # Card background + border (hover changes brightness)
        bg = (40, 40, 40) if not hovered else (65, 65, 65)
        border = (130, 130, 130) if not hovered else (220, 220, 220)

        pygame.draw.rect(screen, bg, rect, border_radius=16)
        pygame.draw.rect(screen, border, rect, width=2, border_radius=16)

        # Bot name
        name_surf = card_title_font.render(bot["name"], True, (230, 230, 230))
        screen.blit(name_surf, (rect.centerx - name_surf.get_width() // 2, rect.y + 30))

        # Subtitle
        sub_surf = card_sub_font.render(bot["subtitle"], True, (180, 180, 180))
        screen.blit(sub_surf, (rect.centerx - sub_surf.get_width() // 2, rect.y + 80))


    pygame.display.flip()


#function to create a new board
def create_board():
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

#function to check for a win
def has_winner(board, currPlayer):
    # Check horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c + i] == currPlayer for i in range(4)):
                return True
    # Check vertical
    for r in range(ROWS - 3):
        for c in range(COLS):
            if all(board[r + i][c] == currPlayer for i in range(4)):
                return True
    # Check diagonal (positive slope)
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r + i][c + i] == currPlayer for i in range(4)):
                return True
    # Check diagonal (negative slope)
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r - i][c + i] == currPlayer for i in range(4)):
                return True
    return False

#function to check for a draw
def check_draw(board):
    return all(board[0][c] != EMPTY for c in range(COLS))
