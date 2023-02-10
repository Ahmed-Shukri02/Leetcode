class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        def oob(i, j):
            return (i < 0 or i >= ROWS) or (j < 0 or j >= COLS)

        hmap = defaultdict(int)   
        q = deque([])
        for i in range(ROWS):
            for j in range(COLS):
                hmap[grid[i][j]] += 1
                if grid[i][j]:
                    q.append((i, j))

        if 0 not in hmap or 1 not in hmap:
            return -1

        d = -1
        while q:
            l = len(q)
            for k in range(l):
                curr_i, curr_j = q.popleft()
                dirs = [(curr_i + 1, curr_j), (curr_i - 1, curr_j), (curr_i, curr_j + 1), (curr_i, curr_j - 1)]
                for new_i, new_j in dirs:
                    if not oob(new_i, new_j) and not grid[new_i][new_j]:
                        grid[new_i][new_j] = 1
                        q.append((new_i, new_j))
            d += 1

        return d