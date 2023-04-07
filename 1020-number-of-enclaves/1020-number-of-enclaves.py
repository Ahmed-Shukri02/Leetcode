class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        f = 0
        ROWS, COLS = len(grid), len(grid[0])
        def oob(i, j):
            return (i < 0 or i >= ROWS) or (j < 0 or j >= COLS)
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:
                    island = True
                    grid[i][j] = 0
                    q = deque([(i, j)])
                    cells = 1
                    while q:
                        l = len(q)
                        for k in range(l):
                            oldi, oldj = q.popleft()
                            dirs = [(oldi + 1, oldj), (oldi - 1, oldj), (oldi, oldj + 1), (oldi, oldj - 1)]
                            for newi, newj in dirs:
                                if oob(newi, newj):
                                    island = False
                                elif grid[newi][newj]:
                                    cells += 1
                                    grid[newi][newj] = 0
                                    q.append((newi, newj))
                    
                    if island: f += cells
        
        return f