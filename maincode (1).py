def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_tie(board):
    return all(cell != ' ' for row in board for cell in row)

def make_move(board, row, col, player):
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    else:
        print("Cell already taken! Try again.")
        return False

def play_game():
    board = initialize_board()
    current_player = 'X'

    while True:
        print_board(board)

        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))
        except ValueError:
            print("Invalid input! Enter numbers between 0 and 2.")
            continue

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Invalid position! Try again.")
            continue

        if not make_move(board, row, col, current_player):
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

play_game()
