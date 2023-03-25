class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = [-1 for i in range(n)]
        
        def find(num):
            while uf[num] >= 0:
                num = uf[num]
            return num

        def union(n1, n2):
            par1, par2 = find(n1), find(n2)
            if par1 == par2:
                return
            
            if uf[par1] < uf[par2]:
                uf[par1] += uf[par2]
                uf[par2] = par1
            else:
                uf[par2] += uf[par1]
                uf[par1] = par2


        for s, d in edges:
            union(s, d)
        
        f = 0
        for num in uf:
            if num < 0:
                f += (-num) * (n + num)
        return f // 2
            