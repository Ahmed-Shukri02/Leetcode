class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n1, n2 = {}, {}
        q1, q2 = deque([node1]), deque([node2])
        visited = set([node1])
        d = 0
        while q1:
            val = q1.popleft()
            if edges[val] != -1 and edges[val] not in visited:
                visited.add(edges[val])
                q1.append(edges[val])
            n1[val] = d
            d += 1
        
        visited = set([node2])
        d = 0
        while q2:
            val = q2.popleft()
            if edges[val] != -1 and edges[val] not in visited:
                visited.add(edges[val])
                q2.append(edges[val])
            n2[val] = d
            d += 1
        
        # find intersection of sets
        m = float("inf")
        f = -1
        for key in set(list(n1.keys()) + list(n2.keys())):
            if key not in n1 or key not in n2:
                continue
            if max(n1[key], n2[key]) < m:
                m = max(n1[key], n2[key])
                f = key

        
        return f
