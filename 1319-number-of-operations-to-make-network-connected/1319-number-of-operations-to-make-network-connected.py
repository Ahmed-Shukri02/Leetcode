class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        uf = [-1 for i in range(n)]
        self.excess = 0

        def find(i):
            while uf[i] >= 0:
                i = uf[i]
            return i

        def union(s, d):
            s_par, d_par = find(s), find(d)
            if s_par == d_par: 
                self.excess += 1
                return 

            if uf[s_par] < uf[d_par]:
                uf[s_par] += uf[d_par]
                uf[d_par] = s_par
            else:
                uf[d_par] += uf[s_par]
                uf[s_par] = d_par


        for s, d in connections:
            union(s, d)
        
        steps = -1
        for par in uf:
            if par < 0: steps += 1

        return steps if self.excess >= steps else -1

        
            