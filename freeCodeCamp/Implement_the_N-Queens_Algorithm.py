"""Implement the N-Queens Algorithm
The N-Queens problem asks you to place N queens on an N×N chessboard so that no two queens attack each other (no two share a row, column, or diagonal).

For example, if there is a 4x4 board, one valid arrangement is:

Example Code
[1, 3, 0, 2]
That means that in row 0, the queen is placed in column 1; in row 1, the queen is placed in column 3; in row 2, the queen is placed in column 0; and in row 3, the queen is placed in column 2.

Visually, this arrangement looks like:

Example Code
. Q . .
. . . Q
Q . . .
. . Q .
Where Q represents a queen and . represents an empty square.

In this lab, you will implement the N-Queens problem solver using the depth-first search approach.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

You should have a function named dfs_n_queens.
The function should accept exactly one argument: an integer n.
If n is less than 1, the function should return an empty list ([]).
The function should return a list of solutions; each solution is itself a list of length n, where the element at index i is the column index (0-based) of the queen in row i.
Run the Tests (Ctrl + Enter)
Reset this lesson
Get Help
Tests

Passed: 1. You should have a function named dfs_n_queens that takes one argument.
Passed: 2. If n is less than 1, the function should return an empty list.
Passed: 3. The function should return a list of solutions, where each solution is a list of length n.
Passed: 4. dfs_n_queens(1) should return [[0]].
Passed: 5. dfs_n_queens(2) should return [].
Passed: 6. dfs_n_queens(3) should return [].
Passed: 7. dfs_n_queens(4) should return [[1, 3, 0, 2], [2, 0, 3, 1]].
Passed: 8. dfs_n_queens(5) should return [[0, 2, 4, 1, 3], [0, 3, 1, 4, 2], [1, 3, 0, 2, 4], [1, 4, 2, 0, 3], [2, 0, 3, 1, 4], [2, 4, 1, 3, 0], [3, 0, 2, 4, 1], [3, 1, 4, 2, 0], [4, 1, 3, 0, 2], [4, 2, 0, 3, 1]].
Passed: 9. len(dfs_n_queens(5)) should be 10.
Passed: 10. len(dfs_n_queens(8)) should be 92."""

def dfs_n_queens(n):
    if not isinstance(n, int):
        return "n should be an integer."
    if n < 1:
        return []
    options = []
    placement = []
    board = [['.'] * n for _ in range(n)]
    
    def not_safe(r, c):
        for row, col in enumerate(placement):
            if col == c or abs(col - c) == abs(row - r):
                return False
        return True

    def place(r):
        if r == n:
            options.append(placement.copy())
            return

        for c in range(n):
            if not_safe(r, c):
                placement.append(c)
                place(r + 1)
                placement.pop()

    place(0)
    return options


print(dfs_n_queens(4))