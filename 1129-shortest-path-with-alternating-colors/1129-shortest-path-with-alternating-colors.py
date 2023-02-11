class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        hmap = defaultdict(set)

        opp = {"r": "b", "b": "r"}

        for s, dest in redEdges:
            hmap[(s, dest)].add("r")
            adj[s].append(dest)
        for s, dest in blueEdges:
            hmap[(s, dest)].add("b")
            adj[s].append(dest)
        
        f = [-1] * n
        q = deque([(0, "r"), (0, "b")])
        d = 0
        visited = set([])
        while q:
            l = len(q)
            for i in range(len(q)):
                curr, prev_col = q.popleft()
                f[curr] = min(f[curr], d) if f[curr] != -1 else d
                for neigh in adj[curr]:
                    if (curr, neigh, prev_col) in visited or opp[prev_col] not in hmap[(curr, neigh)]:
                        continue
                    visited.add((curr, neigh, prev_col))
                    q.append((neigh, opp[prev_col]))
            d += 1
        return f



