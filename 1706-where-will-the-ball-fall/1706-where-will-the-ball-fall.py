class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        ROWS, COLS = len(grid), len(grid[0])
        mem = {}
        def oob(i, j):
            return (i < 0 or i >= ROWS) or (j < 0 or j >= COLS)

        def dfs(i, j, top):
            if i == ROWS:
                return j
            
            if (i, j, top) in mem:
                return mem[(i, j, top)]
            
            ans = None
            if top and grid[i][j] == 1:
                if oob(i, j + 1) or grid[i][j + 1] != grid[i][j]:
                    return -1
                ans = dfs(i, j + 1, 0)
            elif top and grid[i][j] == -1:
                if oob(i, j - 1) or grid[i][j - 1] != grid[i][j]:
                    return -1
                ans = dfs(i, j - 1, 0)
            else:
                # we're on bot, go down
                ans = dfs(i + 1, j, 1)
            
            mem[(i, j, top)] = ans
            return ans
        
        final = [-1] * COLS
        for j in range(COLS):
            final[j] = dfs(0, j, 1)
            
        return final