class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        if not roads:
            return 0
        
        # single source bfs from 0
        adj = defaultdict(list)
        for s, d in roads:
            adj[s].append(d)
            adj[d].append(s)
        
        self.f = 0
        visited = set([0])

        def dfs(node):

            ppl = 0
            for neigh in adj[node]:
                if neigh in visited:
                    continue
                visited.add(neigh)
                # find the amount of cars that arrived here, as well as available space
                ppl += dfs(neigh)
            
            # redistribute people
            cars = ppl // seats
            cars += 1

            if node != 0: self.f += cars
            return ppl + 1
        
        dfs(0)
        return self.f