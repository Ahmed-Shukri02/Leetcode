class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l, r = 0, len(mat[0]) - 1
        f = 0
        for row in mat:
            if l != r: f += row[l] + row[r]
            else: f += row[l]
            l, r = l + 1, r - 1
        return f