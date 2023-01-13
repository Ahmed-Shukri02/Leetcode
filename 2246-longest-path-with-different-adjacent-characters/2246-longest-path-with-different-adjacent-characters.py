class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        adj = {}
        for i in range(len(parent)):
            if parent[i] not in adj: adj[parent[i]] = []
            adj[parent[i]].append(i)
        
        self.m = 0
        def dfs(node):
            if node not in adj: # leaf
                self.m  = max(self.m, 1)
                return 1
            children = [0, 0]
            for child in adj[node]:
                ans = dfs(child)
                if s[child] != s[node]: children.append(ans)
            children = sorted(children, reverse = True)
            single, alt = children[0] + 1, children[0] + children[1] + 1
            self.m = max(self.m, alt)
            return single
        dfs(0)
        return self.m

            
            