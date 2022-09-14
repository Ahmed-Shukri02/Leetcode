class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False for i in range(COLS)] for j in range(ROWS)]
        
        def dfs(i, j):
            if (i < 0 or i >= ROWS) or (j < 0 or j >= COLS) or grid[i][j] == 0 or visited[i][j]:
                return 0
            
            visited[i][j] = True
            counter = 1
            
            return (counter +
                    dfs(i + 1, j, ) + dfs(i - 1, j) +
                    dfs(i, j + 1) + dfs(i, j - 1))
        
        maxArea = 0
        for i in range(ROWS):
            for j in range(COLS):
                    if grid[i][j] == 1 and not visited[i][j]:
                        maxArea = max(maxArea, dfs(i, j))
        return maxArea