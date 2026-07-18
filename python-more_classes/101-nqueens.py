#!/usr/bin/python3
"""Processes matrix paths solving classic non-attacking N Queens
scenarios.
"""
import sys


def solve_nqueens(n, row, board, solutions):
    """Backtracks systematically over placement coordinate matrices."""
    if row == n:
        solutions.append([list(x) for x in board])
        return
    for col in range(n):
        accepted = True
        for r, c in board:
            if c == col or abs(r - row) == abs(c - col):
                accepted = False
                break
        if accepted:
            board.append([row, col])
            solve_nqueens(n, row + 1, board, solutions)
            board.pop()


def main():
    """Processes incoming argument constraints validating numerical bounds."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = []
    solve_nqueens(n, 0, [], solutions)
    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    main()
