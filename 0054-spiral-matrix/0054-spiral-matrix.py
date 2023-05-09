class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        f = []
        i, j = 0, 0
        while min(m, n) > 0:
            if m == 1:
                for k in range(n):
                    f.append(matrix[i][j])
                    j += 1
                break
            elif n == 1:
                for k in range(m):
                    f.append(matrix[i][j])
                    i += 1
                break

            for k in range(n):
                f.append(matrix[i][j])
                j += 1
            i, j = i + 1, j - 1
            for k in range(m - 1):
                f.append(matrix[i][j])
                i += 1
            i, j = i - 1, j - 1
            for k in range(n - 1):
                f.append(matrix[i][j])
                j -= 1
            i, j = i - 1, j + 1
            for k in range(m - 2):
                f.append(matrix[i][j])
                i -= 1
            i, j = i + 1, j + 1
            m, n = m - 2, n - 2
        
        return f