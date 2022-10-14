class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # two pointer
        length = len(prices)
        l, r = 0, 1
        maxProfit = 0
        while l < r and r < length:
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                if profit > maxProfit:
                    maxProfit = profit
                r += 1
            else:
                l = r
                r += 1
        return maxProfit