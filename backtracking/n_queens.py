# N-Queens Problem
# Place n queens on an n x n chessboard so that no two queens attack each other.
# Uses backtracking with column, diagonal, and anti-diagonal tracking.
# Time Complexity: O(n!) | Space Complexity: O(n)
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: integer n
# Output: all solutions as board layouts separated by blank lines, followed by total count

import sys
input = sys.stdin.readline


def solve_n_queens(n):
    solutions = []
    queens = [0] * n  # queens[row] = column
    cols = set()
    diag = set()       # row - col
    anti_diag = set()   # row + col

    def backtrack(row):
        if row == n:
            board = []
            for r in range(n):
                line = ['.' * queens[r] + 'Q' + '.' * (n - queens[r] - 1)]
                board.append(line[0])
            solutions.append(board)
            return
        for col in range(n):
            if col in cols or (row - col) in diag or (row + col) in anti_diag:
                continue
            queens[row] = col
            cols.add(col)
            diag.add(row - col)
            anti_diag.add(row + col)
            backtrack(row + 1)
            cols.remove(col)
            diag.remove(row - col)
            anti_diag.remove(row + col)

    backtrack(0)
    return solutions


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        solutions = solve_n_queens(n)
        for i, board in enumerate(solutions):
            if i > 0:
                print()
            for row in board:
                print(row)
        print(f"Total: {len(solutions)}")


if __name__ == "__main__":
    main()
