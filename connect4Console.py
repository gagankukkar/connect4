P1PIECE = 1
P2PIECE = 2

ROW_TOT = 6
COL_TOT = 7


def board_printer(board):
    for row in reversed(range(6)):
        print(row, board[row])
    print('  ---------------------')
    print('   0  1  2  3  4  5  6')


def turn_input(board, player, piece):
    while True:
        try:
            col = int(input(f'Enter column location {player} : '))
            if 0 <= col <= 6:
                for row in range(6):
                    if board[row][col] == 0:
                        board[row][col] = piece
                        return True
                    else:
                        if row == 5:
                            print('This column is full! Pick another spot.')
                            return False
                        continue
            else:
                print('Value must be between 0 to 6!')
        except ValueError:
            print('Not a valid input!')


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


def game():
    print('Welcome to Connect 4!')

    player1 = input('Player 1, enter your name: ')
    player2 = input('Player 2, enter your name: ')

    while player1 == player2:
        print('Players must have different names!')
        player2 = input('Player 2, enter your name: ')

    board = []
    for row in range(6):
        board.append([0, 0, 0, 0, 0, 0, 0])

    board_printer(board)

    for turn in range(42):
        if turn % 2 == 0:
            current_turn = turn_input(board, player1, P1PIECE)
            while not current_turn:
                current_turn = turn_input(board, player1, P1PIECE)
        else:
            current_turn = turn_input(board, player2, P2PIECE)
            while not current_turn:
                current_turn = turn_input(board, player2, P2PIECE)

        board_printer(board)

        if turn < 6:
            continue

        elif check_win(board, P1PIECE):
            print(f'{player1} wins!')
            break

        elif check_win(board, P2PIECE):
            print(f'{player2} wins!')
            break

        elif turn == 41:
            print('Tie game!')

if __name__ == '__main__':
     game()