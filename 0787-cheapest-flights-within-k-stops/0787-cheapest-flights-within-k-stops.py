class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        c = [float("inf")] * n
        c[src] = 0
        for i in range(k + 1):
            tmp = c.copy()
            for s, d, p in flights:
                tmp[d] = min(tmp[d], c[s] + p)
            c = tmp
        return -1 if c[dst] == float("inf") else c[dst]

            