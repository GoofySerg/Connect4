import pygame
import sys
import connect4 as c4
import ai as ai

pygame.init()

WIDTH, HEIGHT = 700, 600
ROWS, COLS = 5, 7
TOP_MARGIN = 100
pieces = [0] * COLS
board = c4.create_board()
currPlayer = c4.P1
game_over = False
game_started = False
winne = None

CELL_SIZE = WIDTH // COLS
RADIUS = CELL_SIZE // 2 - 8

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect Four")
clock = pygame.time.Clock()

while True: 
    
    #menu screen
    if not game_started:
        c4.draw_bot_menu(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                for rect, bot in c4.menu_cards:
                    if rect.collidepoint(mx, my):
                        selected_bot = bot["id"]
                        bot_depth = bot["depth"]
                        game_started = True
                        break

        continue








    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #generate the board again
        if event.type == pygame.KEYDOWN and game_started:
            if event.key == pygame.K_r:
                pieces = [0] * COLS
                board = c4.create_board()
                game_over = False
                currPlayer = 1

        #human move
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and game_started and currPlayer == c4.P1 and not game_over:
            mx, my = event.pos
            if my < TOP_MARGIN:
                col = mx // CELL_SIZE
                if col in c4.get_valid_moves(board):
                    
                    c4.drop_piece(board, col, currPlayer)
                    
                    if c4.has_winner(board, currPlayer):
                        game_over = True
                        winner = currPlayer
                    elif c4.check_draw(board):
                        game_over = True
                        winner = 0  # draw
                    else:
                        currPlayer = c4.P2 if currPlayer == c4.P1 else c4.P1
            
    # AI move
    if currPlayer == c4.P2 and not game_over and game_started:
        col = ai.make_optimal_move(board, depth=bot_depth)
        if col is not None:
            c4.drop_piece(board, col, currPlayer)
            if c4.has_winner(board, currPlayer):
                game_over = True
                winner = currPlayer
            elif c4.check_draw(board):
                game_over = True
                winner = 0  # draw
            else:
                currPlayer = c4.P1


   



    screen.fill((25, 25, 25))  # background

    # board first
    board_rect = pygame.Rect(0, TOP_MARGIN, WIDTH, HEIGHT - TOP_MARGIN)
    pygame.draw.rect(screen, (0, 90, 200), board_rect)

    if c4.has_winner(board, c4.P1):
        pygame.draw.rect(screen, (50, 200, 50), board_rect) 
        
        
    if c4.has_winner(board, c4.P2):
        pygame.draw.rect(screen, (200, 50, 50), board_rect)


    # draw holes on top
    for r in range(ROWS):
        for c in range(COLS):
            cx = c * CELL_SIZE + CELL_SIZE // 2
            cy = TOP_MARGIN + r * CELL_SIZE + CELL_SIZE // 2
            pygame.draw.circle(screen, (15, 15, 15), (cx, cy), RADIUS)


    # draw placed pieces next (so holes can sit on top)
    for r in range(ROWS):
        for col in range(COLS):
            val = board[r][col]
            if val == 0:
                continue
            x = col * CELL_SIZE + CELL_SIZE // 2
            y = TOP_MARGIN + r * CELL_SIZE + CELL_SIZE // 2
            if val == 1:
                pygame.draw.circle(screen, (240, 240, 40), (x, y), RADIUS)
            else:
                pygame.draw.circle(screen, (220, 50, 50), (x, y), RADIUS)

    
    # hover preview
    mx, my = pygame.mouse.get_pos()
    if my < TOP_MARGIN and not game_over and currPlayer == c4.P1:
        col = mx // CELL_SIZE
        if 0 <= col < COLS:
            hx = col * CELL_SIZE + CELL_SIZE // 2
            preview_color = (240, 240, 40) if currPlayer == 1 else (220, 50, 50)
            pygame.draw.circle(screen, preview_color, (hx, TOP_MARGIN // 2), RADIUS)

    pygame.display.flip()
    clock.tick(60)

