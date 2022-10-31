class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        m, n = len(matrix), len(matrix[0])
        
        def oob(i, j):
            return (i < 0 or i >= m) or (j < 0 or j >= n)
                
        def check(i, j):
            num = matrix[i][j]
            while not oob(i, j):
                if matrix[i][j] != num:
                    return False
                i, j = i + 1, j + 1
            return True
        
        for j in range(n):
            if not check(0, j):
                return False
        for i in range(m):
            if not check(i, 0):
                return False
        
        return True