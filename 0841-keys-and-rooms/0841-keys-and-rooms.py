class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        
        # bfs
        q = deque([0])
        r = set([0])
        
        while q:
            l = len(q)
            for i in range(l):
                for key in rooms[q[i]]:
                    if key not in r:
                        r.add(key)
                        q.append(key)
            for i in range(l):
                q.popleft()
        
        return len(r) == n