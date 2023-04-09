class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n, visited = len(colors), 0
        arr, indegree = [], [0 for i in range(n)]
        adj = defaultdict(list)
        for s, d in edges:
            adj[s].append(d)
            indegree[d] += 1
        
        q = deque([])
        for i in range(n): # add any nodes with no dependencies
            if not indegree[i]:
                q.append(i)

        while q:
            node = q.popleft()
            arr.append(node)
            visited += 1

            for neigh in adj[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)

        if visited < n:
            return - 1
        
        print(arr)
        dp = {i: {} for i in range(n)}

        for i in range(n - 1, -1, -1):
            index = arr[i]
            for a in adj[index]:
                for col in dp[a].keys():
                    dp[index][col] = max(dp[index].get(col, 0), dp[a][col])
            dp[index][colors[index]] = dp[index].get(colors[index], 0) + 1

        return max([max(i.values()) for i in dp.values()])


            