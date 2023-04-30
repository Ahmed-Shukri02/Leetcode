class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        uf = [-1 for i in range(len(strs))]
        self.f = len(strs)
        def find(a):
            while uf[a] >= 0:
                a = uf[a]
            return a

        def union(a, b):
            p1, p2 = find(a), find(b)
            if p1 == p2:
                return
            if uf[p1] > uf[p2]:
                uf[p2] += uf[p1]
                uf[p1] = p2
            else:
                uf[p1] += uf[p2]
                uf[p2] = p1
            self.f -= 1

        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                switched = 0
                for k in range(len(strs[i])):
                    switched += strs[i][k] != strs[j][k]
                if switched in (2, 0):
                    union(i, j)
        
        return self.f