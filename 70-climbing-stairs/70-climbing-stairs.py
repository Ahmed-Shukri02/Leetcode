class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [None] * n
        
        def dfs(m):
            if m == n:
                return 1
            elif m > n:
                return 0
            
            if res[m]:
                return res[m]
            
            # choose to do 2 steps or one
            ans = dfs(m + 2) + dfs(m + 1)
            res[m] = ans
            return ans

        return dfs(0)