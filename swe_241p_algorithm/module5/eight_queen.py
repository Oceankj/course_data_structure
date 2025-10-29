def is_valid(board: list[int]) -> bool:
    return (
        is_col_valid(board)
        and is_diagonal_valid(board)
        and is_anti_diagonal_valid(board)
    )


def is_col_valid(board: list[int]) -> bool:
    cols = [0] * 9
    for col in board:
        if col == 0:
            continue
        if cols[col] == 1:
            return False
        cols[col] = 1
    return True


def is_diagonal_valid(board: list[int]) -> bool:
    # Check that no two queens are on the same main diagonal (col - row is equal)
    diag = [0] * 16  # Possible values for (col - row): -7 to 7, we shift by +7
    for row in range(8):
        col = board[row]
        if col == 0:
            continue
        index = col - row + 7
        if diag[index] == 1:
            return False
        diag[index] = 1
    return True


def is_anti_diagonal_valid(board: list[int]) -> bool:
    # Check that no two queens are on the same anti-diagonal (row + col are equal)
    anti_diag = [0] * 16  # Possible values for (row + col): 0 to 15
    for row in range(8):
        col = board[row]
        if col == 0:
            continue
        index = row + col
        if anti_diag[index] == 1:
            return False
        anti_diag[index] = 1
    return True


def backtrack(
    board: list[int], row: int, diff: int, min_diff: list[int], input
):
    if diff >= min_diff[0]:
        return

    if row == 8:
        min_diff[0] = min(diff, min_diff[0])
        return

    for col in range(1, 9):
        board[row] = col
        needed_move = 0 if input[row] == board[row] else 1
        diff += needed_move
        if is_valid(board):
            backtrack(board, row + 1, diff, min_diff, input)
        board[row] = 0
        diff -= needed_move


def eight_queen(input: list[int]) -> int:
    min_diff: list[int] = [8]
    board = [0] * 8
    backtrack(board, 0, 0, min_diff, input)
    return min_diff[0]
