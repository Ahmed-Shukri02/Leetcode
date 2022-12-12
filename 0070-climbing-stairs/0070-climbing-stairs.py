class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        # bottom up dp
        prev1, prev2 = 1, 2
        
        for i in range(n - 2):
            ans = prev1 + prev2
            prev1, prev2 = prev2, ans
        
        return prev2