import random

def initialize_board(rows, cols, mines):
    # Create an empty board
    board = [[' ' for _ in range(cols)] for _ in range(rows)]

    # Place mines randomly on the board
    mine_positions = random.sample(range(rows * cols), mines)
    for mine_position in mine_positions:
        row = mine_position // cols
        col = mine_position % cols
        board[row][col] = 'X'

    return board

def print_board(board, show_mines=False):
    for row in board:
        print(' '.join(cell if cell != 'X' or show_mines else ' ' for cell in row))

def count_adjacent_mines(board, row, col):
    mine_count = 0
    for i in range(max(0, row - 1), min(len(board), row + 2)):
        for j in range(max(0, col - 1), min(len(board[0]), col + 2)):
            if board[i][j] == 'X':
                mine_count += 1
    return mine_count

def reveal_empty_cells(board, revealed, row, col):
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or revealed[row][col]:
        return

    revealed[row][col] = True

    if board[row][col] == ' ':
        for i in range(max(0, row - 1), min(len(board), row + 2)):
            for j in range(max(0, col - 1), min(len(board[0]), col + 2)):
                reveal_empty_cells(board, revealed, i, j)

def minesweeper():
    rows, cols, mines = 6, 6, 10
    board = initialize_board(rows, cols, mines)
    revealed = [[False for _ in range(cols)] for _ in range(rows)]

    while True:
        print_board(revealed)

        row = int(input("Enter row (0 to {}): ".format(rows - 1)))
        col = int(input("Enter column (0 to {}): ".format(cols - 1)))

        if board[row][col] == 'X':
            print("Game Over! You hit a mine.")
            print_board(board, show_mines=True)
            break
        else:
            mine_count = count_adjacent_mines(board, row, col)
            board[row][col] = str(mine_count) if mine_count > 0 else ' '
            revealed[row][col] = True

            if mine_count == 0:
                reveal_empty_cells(board, revealed, row, col)

            if all(all(cell != ' ' for cell in row) for row in revealed):
                print("Congratulations! You won!")
                break

# Run the Minesweeper game
minesweeper()
