class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False for i in range(COLS)] for i in range(ROWS)]
        
        def dfs(i, j):
            # if i or j is out of bounds
            if (i < 0 or i >= ROWS) or (j < 0 or j >= COLS) or visited[i][j] or grid[i][j] == "0":
                return
            # not out of bounds, value 1, not visited and adjacent to land
            visited[i][j] = True
            
            # run in all 4 directions
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        
        islands = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and not visited[i][j]:
                    islands += 1
                    dfs(i, j)
        return islands