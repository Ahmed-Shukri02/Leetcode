class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        
        rowStrength =[]
        for i, row in enumerate(mat):
            rowStrength.append((sum(row), i))
            
        kWeakest = sorted(rowStrength)[:k]
        return [i[1] for i in kWeakest]
