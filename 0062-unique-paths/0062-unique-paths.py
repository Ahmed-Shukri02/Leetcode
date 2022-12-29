class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        mem = [[None for i in range(n)] for i in range(m)]
        visited = [[False for i in range(n)] for i in range(m)]
        ways = []
        
        def oob(i, j):
            return (i < 0 or i >= m) or (j < 0 or j >= n)
        
        def dfs(i, j):
            if oob(i, j) or visited[i][j]:
                return 0
            elif i == m-1 and j == n-1:
                return 1
            
            if mem[i][j] != None:
                return mem[i][j]
            
            visited[i][j] = True
            res = 0
            dirs = [(i + 1, j), (i, j + 1)]
            for newi, newj in dirs:
                res += dfs(newi, newj)
            
            visited[i][j] = False
            mem[i][j] = res
            return res
        
        return dfs(0, 0)