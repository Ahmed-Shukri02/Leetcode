class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        f = 0
        ROWS, COLS = len(grid), len(grid[0])

        def oob(i, j):
            return (i < 0 or i >= ROWS) or (j < 0 or j >= COLS)

        visited = set([])
        for i in range(ROWS):
            for j in range(COLS):
                if not grid[i][j] and (i, j) not in visited:
                    # do bfs
                    visited.add((i, j))
                    q = deque([(i, j)])
                    island = True
                    while q:
                        l = len(q)
                        for k in range(l):
                            oldi, oldj = q.popleft()
                            dirs = [(oldi + 1, oldj), (oldi - 1, oldj), (oldi, oldj + 1), (oldi, oldj - 1)]
                            for newi, newj in dirs:
                                if oob(newi, newj):
                                    # not surrounded by water
                                    island = False
                                    continue
                                if (newi, newj) in visited:
                                    continue
                                elif not grid[newi][newj]:
                                    visited.add((newi, newj))
                                    q.append((newi, newj))
                    if island: f += 1
        return f

