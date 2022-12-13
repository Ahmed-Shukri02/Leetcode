class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        mem = {}
        
        def dfs(i, j):
            if j >= COLS or j < 0:
                return float("inf")
            elif i >= ROWS:
                return 0
            
            if (i, j) not in mem:
                l, r, c = dfs(i + 1, j - 1), dfs(i + 1, j + 1), dfs(i + 1, j)
                mem[(i, j)] = matrix[i][j] + min(l, r , c)
            
            return mem[(i, j)]
        
        final = float("inf")
        for j in range(COLS):
            final = min(final, dfs(0, j))
        return final