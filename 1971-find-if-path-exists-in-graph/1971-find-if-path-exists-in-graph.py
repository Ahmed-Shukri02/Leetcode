class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if not edges:
            return source == destination
        
        hmap = {}
        # turn to adjacency map
        for s, d in edges:
            if s not in hmap:
                hmap[s] = []
            if d not in hmap:
                hmap[d] = []
            
            hmap[s].append(d)
            hmap[d].append(s)
        
        # do bfs of source until either exhausted or destination found
        q = deque([source])
        bl = set()
        while q:
            l = len(q)
            for i in range(l):
                bl.add(q[i])
                for d in hmap[q[i]]:
                    if d == destination:
                        return True
                    if d not in bl:
                        q.append(d)
            for i in range(l):
                q.popleft()
        return False