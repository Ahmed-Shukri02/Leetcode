class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        visited = [[False for i in range(COLS)] for i in range(ROWS)]
        uncaptured = set()
        
        def dfs(i, j):
            # return if out of bounds or visited
            if (i < 0 or i >= ROWS) or (j < 0 or j >= COLS) or visited[i][j]:
                return
            if board[i][j] == "X":
                return
            
            visited[i][j] = True
            uncaptured.add((i, j))
            
            dirs = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            for newi, newj in dirs:
                dfs(newi, newj)
        
        # run dfs around perimeter
        for i in range(ROWS):
            dfs(i, 0)
            dfs(i, COLS -1)
        for j in range(COLS):
            dfs(0, j)
            dfs(ROWS - 1, j)
        
        # turn everything in board to X
        for i in range(ROWS):
            for j in range(COLS):
                board[i][j] = "X"
        
        # turn everything in set to O
        for i, j in uncaptured:
            board[i][j] = "O"
        