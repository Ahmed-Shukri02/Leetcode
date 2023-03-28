class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0 for i in range(days[-1])]
        dp.append(0)
        days = set(days)
        for i in range(1, len(dp)):
            if i not in days:
                dp[i] = dp[i - 1]
                continue
            o, s, t = max(i - 1, 0), max(i - 7, 0), max(i - 30, 0)
            dp[i] += min(costs[0] + dp[o], costs[1] + dp[s], costs[2] + dp[t])
        
        return dp[-1]