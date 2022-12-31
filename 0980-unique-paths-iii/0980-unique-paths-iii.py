class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def oob(i, j):
            return (i < 0 or i >= ROWS) or (j < 0 or j >= COLS)

        starti, startj = 0, 0
        n = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] in (0, 1):
                    n += 1
                if grid[i][j] == 1:
                    starti, startj = i, j
        
        visited = set()
        self.l = 0
        def dfs(i, j):
            if oob(i, j) or (i, j) in visited or grid[i][j] == -1:
                return 0
            elif grid[i][j] == 2:
                return 1 if self.l == n else 0

            visited.add((i, j))
            self.l += 1
            dirs = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
            unique_ways = 0
            for newi, newj in dirs:
                unique_ways += dfs(newi, newj)
            self.l -= 1
            visited.remove((i, j))

            return unique_ways

            
        
        return dfs(starti, startj)

