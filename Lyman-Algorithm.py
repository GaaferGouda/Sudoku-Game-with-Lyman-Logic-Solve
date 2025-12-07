import sys

# Sudoku Game with Lyman Algorithm

SIZE = 9
BOX_SIZE = 3

def print_board(board):
    """Prints the Sudoku board in a readable format."""
    for i in range(SIZE):
        if i % BOX_SIZE == 0 and i != 0:
            print("-" * 21)
        for j in range(SIZE):
            if j % BOX_SIZE == 0 and j != 0:
                print("|", end=" ")
            val = board[i][j]
            print(val if val != 0 else ".", end=" ")
        print()
    print()

def is_valid(board, row, col, num):
    """Checks if placing num in board[row][col] is valid."""
    if num in board[row]:
        return False
    if num in [board[r][col] for r in range(SIZE)]:
        return False
    start_row, start_col = (row // BOX_SIZE) * BOX_SIZE, (col // BOX_SIZE) * BOX_SIZE
    for r in range(start_row, start_row + BOX_SIZE):
        for c in range(start_col, start_col + BOX_SIZE):
            if board[r][c] == num:
                return False
    return True

def find_candidates(board, row, col):
    """Returns a list of valid candidates for a cell."""
    return [n for n in range(1, SIZE + 1) if is_valid(board, row, col, n)]

def lyman_solve(board):
    """Logical elimination solver."""
    changed = True
    while changed:
        changed = False
        for r in range(SIZE):
            for c in range(SIZE):
                if board[r][c] == 0:
                    candidates = find_candidates(board, r, c)
                    if len(candidates) == 1:
                        board[r][c] = candidates[0]
                        changed = True
    return board

def find_empty(board):
    """Finds the next empty cell or returns None."""
    for r in range(SIZE):
        for c in range(SIZE):
            if board[r][c] == 0:
                return r, c
    return None

def backtracking_solve(board):
    """Backtracking algorithm to solve remaining cells."""
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, SIZE + 1):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if backtracking_solve(board):
                return True
            board[row][col] = 0
    return False

def play_game(board):
    """Interactive Sudoku gameplay."""
    while True:
        print_board(board)
        move = input("Enter move as row col num (or 'solve'/'quit'): ").strip().lower()
        if move == "quit":
            print("Goodbye.")
            break
        elif move == "solve":
            lyman_solve(board)
            backtracking_solve(board)
            print("Solved board:")
            print_board(board)
            break
        else:
            try:
                r, c, n = map(int, move.split())
                if 1 <= r <= SIZE and 1 <= c <= SIZE and 1 <= n <= SIZE:
                    if board[r-1][c-1] == 0 and is_valid(board, r-1, c-1, n):
                        board[r-1][c-1] = n
                    else:
                        print("Invalid move.")
                else:
                    print("Values must be between 1 and 9.")
            except ValueError:
                print("Invalid input format.")

puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if __name__ == "__main__":
    play_game(puzzle)
