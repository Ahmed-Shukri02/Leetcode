class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        adjMap = {}
        for s, d in edges:
            if s not in adjMap:
                adjMap[s] = []
            if d not in adjMap:
                adjMap[d] = []
            adjMap[s].append(d)
            adjMap[d].append(s)
        
        bl = set()
        def dfs(node, par):
            f = 0
            for child in adjMap[node]:
                if child != par:
                    f += dfs(child, node)
            if f or hasApple[node]:
                f += 2
            return f
        return max(dfs(0, -1) - 2, 0)
