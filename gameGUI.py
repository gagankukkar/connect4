import sys
import pygame
pygame.init()

#  Spacing and sizing of board
ROW_TOT = 6
COL_TOT = 7
PITCH = 100

#  Define size of board
width = COL_TOT * PITCH
height = (ROW_TOT + 1) * PITCH

#  Create board
size = (width, height)
screen = pygame.display.set_mode(size)

#  Define colours
GREEN = 142, 225, 102
BLUE = 0, 100, 240
BLACK = 0, 0, 0
RED = 240, 60, 0

#  Game data
P1PIECE = 1
P2PIECE = 2

board = []
for row in range(ROW_TOT):
    board.append([0, 0, 0, 0, 0, 0, 0])

turn = 0

#  Initialize font for text
pygame.font.init()
font = pygame.font.SysFont(None, 140)

#  Draw board background
screen.fill(GREEN)
pygame.draw.rect(screen, BLACK, (0, 0, width, PITCH))

for col in range(COL_TOT + 1):
    # Solve beginning edge case
    if col == 0:
        pygame.draw.rect(screen, BLACK, (col*PITCH, 0, 4, height))
    else:
        pygame.draw.rect(screen, BLACK, (col*PITCH, 0, 2, height))
    # Solve end edge case
    if col == COL_TOT:
        pygame.draw.rect(screen, BLACK, (col*PITCH-4, 0, 4, height))
    else:
        pygame.draw.rect(screen, BLACK, (col * PITCH - 2, 0, 2, height))


def board_draw():
    for row in range(ROW_TOT):
        for col in range(COL_TOT):
            triangle = [(int(col * PITCH + PITCH / 2), int(height - (row * PITCH) - PITCH + 5)),
                        (int(col * PITCH + 5), int(height - (row * PITCH) - 5)),
                        (int(col * PITCH + PITCH - 5), int(height - (row * PITCH) - 5))]
            if board[row][col] == 1:
                pygame.draw.polygon(screen, BLUE, triangle)
            if board[row][col] == 2:
                pygame.draw.polygon(screen, RED, triangle)
            if board[row][col] == 0:
                pygame.draw.polygon(screen, BLACK, triangle)


def turn_input(click, board, piece):
    while True:
        col = int(click/PITCH)
        for row in range(ROW_TOT):
            if board[row][col] == 0:
                board[row][col] = piece
                return True
            elif row == 5:
                return False


def check_win(board, piece):
    for row in range(ROW_TOT):
        for col in range(COL_TOT - 3):
            if board[row][col] == piece and board[row][col] == board[row][col + 1] == board[row][col + 2] \
                    == board[row][col + 3]:
                return True

    for row in range(ROW_TOT - 3):
        for col in range(COL_TOT):
            if board[row][col] == piece and board[row][col] == board[row + 1][col] == board[row + 2][col] \
                    == board[row + 3][col]:
                return True

    for row in range(ROW_TOT - 3):
        for col in range(COL_TOT - 3):
            if board[row][col] == piece and board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] \
                    == board[row + 3][col + 3]:
                return True

            elif board[row + 3][col] == piece and board[row + 3][col] == board[row + 2][col + 1] \
                    == board[row + 1][col + 2] == board[row][col + 3]:
                return True


def end_printer(colour, piece):
    if turn == 42:
        winner = font.render('Tie game!', True, colour)
        screen.blit(winner, (120, 0))
    else:
        winner = font.render('Player ' + str(piece) + ' wins!', True, colour)
        screen.blit(winner, (14, 0))

    pygame.display.update()
    pygame.time.wait(4000)
    sys.exit()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if turn == 0:
            welcome = font.render('Welcome!', True, GREEN)
            screen.blit(welcome, (119, 0))

        elif turn == 1:
            pygame.draw.rect(screen, BLACK, (0, 0, width, PITCH))

        board_draw()
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            click = event.pos[0]
            if turn % 2 == 0:
                current_turn = turn_input(click, board, P1PIECE)
                while not current_turn:
                    current_turn = turn_input(click, board, P1PIECE)
            else:
                current_turn = turn_input(click, board, P2PIECE)
                while not current_turn:
                    current_turn = turn_input(click, board, P2PIECE)

            turn += 1
            board_draw()
            pygame.display.update()

            if turn < 7:
                continue

            elif check_win(board, P1PIECE):
                end_printer(BLUE, P1PIECE)

            elif check_win(board, P2PIECE):
                end_printer(RED, P2PIECE)

            elif turn == 42:
                end_printer(GREEN, P1PIECE)
