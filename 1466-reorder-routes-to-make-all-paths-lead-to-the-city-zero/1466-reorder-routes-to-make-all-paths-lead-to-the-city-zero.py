class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        hset = set([tuple(i) for i in connections])
        adj = defaultdict(list)
        for s, d in connections:
            adj[s].append(d)
            adj[d].append(s)
        
        visited = set([0])
        q = deque([0])
        f = 0
        while q:
            l = len(q)
            for i in range(l):
                node = q.popleft()
                for neigh in adj[node]:
                    if neigh in visited:
                        continue
                    visited.add(neigh)
                    q.append(neigh)
                    if (node, neigh) in hset:
                        f += 1
        return f