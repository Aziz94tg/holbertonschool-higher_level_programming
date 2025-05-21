#!/usr/bin/python3
"""Solves the N Queens problem"""
import sys


def is_safe(row, col, solution):
    """Check if a queen can be placed at (row, col)"""
    for r, c in enumerate(solution):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_nqueens(n, row=0, solution=[], solutions=[]):
    """Recursive backtracking solution for N queens"""
    if row == n:
        solutions.append([[r, c] for r, c in enumerate(solution)])
        return

    for col in range(n):
        if is_safe(row, col, solution):
            solve_nqueens(n, row + 1, solution + [col], solutions)


def main():
    """Main function to parse arguments and call solver"""
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
    solve_nqueens(n, solutions=solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
