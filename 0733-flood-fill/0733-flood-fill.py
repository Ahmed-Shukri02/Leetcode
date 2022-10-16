class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        ROWS, COLS = len(image), len(image[0])
        visited = [[False for i in range(COLS)] for i in range(ROWS)]
        col = image[sr][sc]
        
        def dfs(i, j):
            if (i < 0 or i >= ROWS) or (j < 0 or j >= COLS) or visited[i][j] or image[i][j] != col:
                return
            
            visited[i][j] = True
            image[i][j] = color
            
            dirs = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            for newi, newj in dirs:
                dfs(newi, newj)
        
        dfs(sr, sc)
        return image