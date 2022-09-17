class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        rotten, fresh = 0, 0
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        counter = 0
        while q:
            for k in range(len(q)):
                i, j = q[0][0], q[0][1]
                dirs = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
                for newi, newj in dirs:
                    if (newi < 0 or newi >= ROWS) or (newj < 0 or newj >= COLS) or grid[newi][newj] != 1:
                        continue
                    grid[newi][newj] = 2
                    rotten += 1
                    q.append((newi, newj))
                q.popleft()
            counter += 1
        return counter - 1 if rotten == fresh else -1 