class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for s, d, dist in roads:
            adj[s].append((d, dist))
            adj[d].append((s, dist))

        visited = set([1])
        q = deque([1])
        f = float("inf")
        while q:
            l = len(q)
            for i in range(l):
                node = q.popleft()
                for neigh, dist in adj[node]:
                    f = min(f, dist)
                    if neigh in visited:
                        continue
                    visited.add(neigh)
                    q.append(neigh)
                
        return f