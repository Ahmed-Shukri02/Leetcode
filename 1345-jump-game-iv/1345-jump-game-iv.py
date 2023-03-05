class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return len(arr) - 1
        
        h1 = defaultdict(set)
        for i in range(len(arr)):
            h1[arr[i]].add(i)
        
        visited = set()
        q = deque([0])
        target = len(arr) - 1
        d = 0
        while q:
            l = len(q)
            for i in range(l):
                node = q.popleft()
                if node == target:
                    return d
                for neigh in h1[arr[node]]:
                    if neigh in visited:
                        continue
                    visited.add(neigh)
                    q.append(neigh)
                if node - 1 >= 0 and node - 1 not in visited:
                    visited.add(node - 1)
                    q.append(node - 1)
                if node + 1 < len(arr) and node + 1 not in visited:
                    visited.add(node + 1)
                    q.append(node + 1)
                h1[arr[node]] = set()
                
            d += 1

        return -1
