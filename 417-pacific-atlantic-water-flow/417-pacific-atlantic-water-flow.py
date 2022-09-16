class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        
        ROWS, COLS = len(heights), len(heights[0])
        final = []
        isPacific = [[False for i in range(COLS)] for i in range(ROWS)]
        isAtlantic = [[False for i in range(COLS)] for i in range(ROWS)]
        visited = [[False for i in range(COLS)] for i in range(ROWS)]
        
        def dfs(i, j, ocean):
            if visited[i][j]:
                return
            
            visited[i][j] = True
            if ocean == "pacific":
                isPacific[i][j] = True
            elif ocean == "atlantic":
                isAtlantic[i][j] = True
            
            dirs = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            for newi, newj in dirs:
                oob = (newi < 0 or newi >= ROWS) or (newj < 0 or newj >= COLS)
                if not oob and heights[newi][newj] >= heights[i][j]:
                    dfs(newi, newj, ocean)
                    
        # do dfs along pacific line
        for i in range(ROWS):
            dfs(i, 0, "pacific")
        for j in range(COLS):
            dfs(0, j, "pacific")
            
        visited = [[False for i in range(COLS)] for i in range(ROWS)]
        # do dfs along atlantic line
        for i in range(ROWS):
            dfs(i, COLS - 1, "atlantic")
        for j in range(COLS):
            dfs(ROWS - 1, j, "atlantic")
        
        for i in range(ROWS):
            for j in range(COLS):
                if isPacific[i][j] and isAtlantic[i][j]:
                    final.append([i, j])
        return final
        