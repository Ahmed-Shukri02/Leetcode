class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # O(n*m)
        
        adj = {}
        for s, d in edges:
            if s not in adj: adj[s] = []
            if d not in adj: adj[d] = []
            adj[s].append(d)
            adj[d].append(s)
        

        final = [0] * n

        visited = set()
        def dfs(node):
            f = {}
            if node >= n:
                return f
            visited.add(node)

            f[labels[node]] = f.get(labels[node], 0) + 1
            for child in adj[node]:
                if child in visited: continue
                childMap = dfs(child)

                for key in childMap.keys():
                    f[key] = f.get(key, 0) + childMap[key]
            
            final[node] = f[labels[node]]
            return f


        dfs(0)
        return final