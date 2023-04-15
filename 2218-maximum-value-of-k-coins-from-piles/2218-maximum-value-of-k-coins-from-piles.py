class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        mem = {}
        pref = [[0 for j in range(len(piles[i]) + 1)] for i in range(len(piles))]
        for i in range(len(pref)):
            pile = pref[i]
            for j in range(1, len(pile)):
                pref[i][j] = pref[i][j - 1] + piles[i][j-1]

        def dfs(i, k):
            if k <= 0 or i >= len(piles):
                return 0
            if (i, k) not in mem:
                # pick a number from 0 to max(k, size of pile)
                f = 0
                for j in range(min(k, len(piles[i])) + 1):
                    f = max(f, pref[i][j] + dfs(i + 1, k - j))
                mem[(i, k)] = f
            return mem[(i, k)]

        return dfs(0, k)