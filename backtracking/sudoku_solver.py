# Sudoku Solver
# Solve a 9x9 Sudoku puzzle using backtracking with constraint propagation.
# Empty cells are represented by 0.
# Time Complexity: O(9^(empty cells)) worst case, much faster with pruning
# Space Complexity: O(81) for the board + O(empty cells) recursion depth
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     9 lines of 9 space-separated digits (0 = empty)
# Output: solved 9x9 grid

import sys
input = sys.stdin.readline


def solve_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    empty = []

    for r in range(9):
        for c in range(9):
            if board[r][c] != 0:
                num = board[r][c]
                rows[r].add(num)
                cols[c].add(num)
                boxes[(r // 3) * 3 + c // 3].add(num)
            else:
                empty.append((r, c))

    def backtrack(idx):
        if idx == len(empty):
            return True
        r, c = empty[idx]
        box_id = (r // 3) * 3 + c // 3
        for num in range(1, 10):
            if num not in rows[r] and num not in cols[c] and num not in boxes[box_id]:
                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_id].add(num)
                if backtrack(idx + 1):
                    return True
                board[r][c] = 0
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[box_id].remove(num)
        return False

    backtrack(0)


def main():
    t = int(input())
    for _ in range(t):
        board = []
        for _ in range(9):
            row = list(map(int, input().split()))
            board.append(row)
        solve_sudoku(board)
        for row in board:
            print(*row)


if __name__ == "__main__":
    main()
