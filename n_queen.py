class NQueenProblem:
    N = int(input("Enter the number of queens: "))

    def printSolution(self, board):
        for i in range(self.N):
            for j in range(self.N):
                print(board[i][j], end=" ")
            print()

    def isSafe(self, board, row, col):
        # Check this row on the left side
        for i in range(col):
            if board[row][i] == 1:
                return False

        # Check the upper diagonal on the left side
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # Check the lower diagonal on the left side
        i, j = row, col
        while j >= 0 and i < self.N:
            if board[i][j] == 1:
                return False
            i += 1
            j -= 1

        return True

    def solveNQUtil(self, board, col):
        # Base case: If all queens are placed, return True
        if col >= self.N:
            return True

        # Consider this column and try placing this queen in all rows one by one
        for i in range(self.N):
            if self.isSafe(board, i, col):
                board[i][col] = 1

                if self.solveNQUtil(board, col + 1):
                    return True

                # If placing queen in board[i][col] doesn't lead to a solution, remove the queen
                board[i][col] = 0  # BACKTRACK

        return False

    def solveNQ(self):
        board = [[0 for _ in range(self.N)] for _ in range(self.N)]

        if not self.solveNQUtil(board, 0):
            print("Solution does not exist")
            return False

        self.printSolution(board)
        return True


# Driver program to test above function
if __name__ == "__main__":
    Queen = NQueenProblem()
    Queen.solveNQ()



'''
This code solves the N-Queens problem using a backtracking algorithm. Let's go through the code step by step:

1. The `NQueenProblem` class is defined. The user is prompted to enter the number of queens (`N`).

2. The `printSolution` method takes a `board` as input and prints it. The `board` is a 2D list representing the chessboard, where 1 represents a queen and 0 represents an empty cell.

3. The `isSafe` method checks if it is safe to place a queen at a specific position (`row`, `col`) on the `board`. It checks three conditions:
   - It checks the left side of the current row to ensure that no queens are present, as they would attack each other horizontally.
   - It checks the upper left diagonal to ensure that no queens are present, as they would attack each other diagonally.
   - It checks the lower left diagonal to ensure that no queens are present, as they would attack each other diagonally.

4. The `solveNQUtil` method is a recursive function that solves the N-Queens problem using backtracking. It takes the `board` and the current column `col` as input. It follows the following steps:
   - Base case: If all queens are placed (i.e., `col` is greater than or equal to `N`), it returns `True` to indicate a solution.
   - It tries placing a queen in each row of the current column by calling the `isSafe` method. If it is safe to place a queen at that position, it marks the cell as 1 (queen).
   - It recursively calls `solveNQUtil` for the next column (`col + 1`).
   - If placing the queen in the current position does not lead to a solution, it backtracks by removing the queen from that cell (`board[i][col] = 0`).
   - If none of the positions in the current column lead to a solution, it returns `False`.

5. The `solveNQ` method initializes an empty `board` (2D list) with all cells set to 0. It calls the `solveNQUtil` method to solve the N-Queens problem, starting from column 0. If a solution is found, it prints the solution by calling the `printSolution` method. Otherwise, it prints "Solution does not exist".

6. In the driver program, an instance of the `NQueenProblem` class is created. The `solveNQ` method is called to solve the N-Queens problem and print the solution if it exists.

The N-Queens problem is a classic problem in which the goal is to place N queens on an N x N chessboard in such a way that no two queens attack each other. The code uses backtracking to explore all possible configurations until a valid solution is found or all possibilities have been exhausted.
'''