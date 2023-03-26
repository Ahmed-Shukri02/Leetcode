class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        adj = defaultdict(list)
        for s in range(len(edges)):
            adj[s].append(edges[s])

        f = -1
        s_visited = set()
        for s in range(len(edges)):
            hmap = {}
            q = deque([s])
            d = 0
            while q:
                l = len(q)
                for i in range(len(q)):
                    node = q.popleft()
                    if node in s_visited: # the max cycle has already been calculated from this node
                        q = []
                        break
                    hmap[node] = min(hmap.get(node, float("inf")), d)
                    for neigh in adj[node]:
                        if neigh in hmap:
                            # cycle has been found
                            f = max(f, d - hmap[neigh] + 1)
                            continue
                        q.append(neigh)
                d += 1
            
            s_visited.add(s)
        
        return f
                    