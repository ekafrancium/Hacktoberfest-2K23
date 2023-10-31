def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N, 1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens_util(board, row, N, solutions):
    if row == N:
        # All queens are placed successfully
        # Add the solution to the list of solutions
        solutions.append(["".join(["Q" if col == 1 else "." for col in row]) for row in board])
        return
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, N, solutions)
            board[row][col] = 0  # Backtrack

def solve_nqueens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)
    return solutions

# Example usage
N = 4  # Change N to solve N-Queens for a different board size
solutions = solve_nqueens(N)
for solution in solutions:
    for row in solution:
        print(row)
    print()
