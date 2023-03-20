class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        mem = {} # mem[(i, k, prev)] = can I put k flowers from i onwards with a previous value of prev?

        def dfs(i, k, prev):
            if i >= len(flowerbed):
                return k == 0
            elif k == 0:
                return True

            if (i, k, prev) not in mem:
                if prev == flowerbed[i] == flowerbed[min(i + 1, len(flowerbed) - 1)] == 0:
                    flowerbed[i] = 1
                    mem[(i, k, prev)] = dfs(i + 1, k - 1, 1)
                else:
                    mem[(i, k, prev)] = dfs(i + 1, k, flowerbed[i])

            return mem[(i, k, prev)]

        return dfs(0, n, 0)

            