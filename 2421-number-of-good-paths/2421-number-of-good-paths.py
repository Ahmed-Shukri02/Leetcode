class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:        
        adj = {}
        for s, d in edges:
            if s not in adj: adj[s] = []
            if d not in adj: adj[d] = []
            adj[s].append(d)
            adj[d].append(s)
        
        arr = [-1] * len(vals)
        def find(num):
            while arr[num] >= 0:
                num = arr[num]
            return num
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return
            if arr[p2] < arr[p1]:
                arr[p2] += arr[p1]
                arr[p1] = p2
            else:
                arr[p1] += arr[p2]
                arr[p2] = p1


        hmap = {}
        for i in range(len(vals)):
            if vals[i] not in hmap: hmap[vals[i]] = []
            hmap[vals[i]].append(i)

        f = len(vals)
        for val in sorted(hmap.keys()):
            for node in hmap[val]:
                for neigh in adj.get(node, []):
                    if vals[neigh] <= val:
                        union(neigh, node)
            
            h2 = {}
            for node in hmap[val]:
                par = find(node)
                h2[par] = h2.get(par, 0) + 1 
            
            for occurance in h2.values():
                f += math.comb(occurance, 2)

        return f