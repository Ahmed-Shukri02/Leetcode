class Solution(object):
    def numRollsToTarget(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """
        mem = {}
        def dfs(curr_n, total):
            if total <= 0 or total > (k * curr_n):
                return 0
            if curr_n == 1:
                return 1

            if (total, curr_n) in mem:
                return mem[(total, curr_n)]

            sol = 0
            for i in range(1, k+1):
                sol += dfs(curr_n  - 1, total - i)
            mem[(total, curr_n)] = sol
            return sol

        sol =  dfs(n, target)
        return sol % (10**9 + 7)