class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxC = 0
        l, r = 0, 1
        
        while r < len(prices) and l < r:
            if prices[r] < prices[l]:
                l = r
                r = r + 1
                continue
            else:
                maxC = max(maxC, prices[r] - prices[l])
                r += 1
        return maxC