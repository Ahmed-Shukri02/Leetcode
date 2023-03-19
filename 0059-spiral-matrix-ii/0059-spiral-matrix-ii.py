class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mid = n // 2
        matrix = [[-1 for i in range(n)] for j in range(n)]
        i, j = 0, 0
        matrix[0][0] = 1
        curr = 2
        
        def oob(i, j):
            return (i < 0 or i >= n) or (j < 0 or j >= n)
        
        while not (i == mid and j == mid):
            d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dy, dx in d:
                while not oob(i + dy, j + dx) and matrix[i + dy][j + dx] == -1:
                    matrix[i + dy][j + dx] = curr
                    i, j = i + dy, j + dx
                    curr += 1
            if curr > n ** 2: break
                
        return matrix