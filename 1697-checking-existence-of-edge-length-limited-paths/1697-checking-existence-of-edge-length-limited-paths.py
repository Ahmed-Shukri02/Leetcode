class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        uf = [-1 for i in range(n)]
        queries2 = [[] for i in range(len(queries))]
        for i in range(len(queries)):
            queries2[i] = queries[i]
            queries2[i].append(i)
        queries2 = sorted(queries2, key = lambda x: x[2])
        edgeList = sorted(edgeList, key = lambda x: -x[2])
        

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

        
        f = [-1 for i in range(len(queries))]
        for s, d, lim, i in queries2:
            while edgeList and edgeList[-1][2] < lim:
                cs, cd, cdist = edgeList.pop()
                union(cs, cd)
            f[i] = find(s) == find(d)
        return f
            

