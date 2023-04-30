class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        class UF:
            def __init__(self, n):
                self.uf = [-1 for i in range(n)]
                self.n = n
            def find(self, a):
                while self.uf[a] >= 0:
                    a = self.uf[a]
                return a
            def union(self, a, b):
                p1, p2 = self.find(a), self.find(b)
                if p1 == p2:
                    return 0
                elif self.uf[p1] > self.uf[p2]:
                    self.uf[p2] += self.uf[p1]
                    self.uf[p1] = p2
                else:
                    self.uf[p1] += self.uf[p2]
                    self.uf[p2] = p1
                self.n -= 1
                return 1

        
        
        p1, p2 = UF(n), UF(n)
        f = 0
        for col, s, d in edges:
            if col == 3:
                c1, c2 = p1.union(s - 1, d - 1), p2.union(s - 1, d - 1)
                f += c1 or c2
        for col, s, d, in edges:
            if col == 1:
                f += p1.union(s - 1, d - 1)
            elif col == 2:
                f += p2.union(s - 1, d - 1)
        
        if p1.n > 1 or p2.n > 1:
            return - 1
        
        return len(edges) - f
        

        

