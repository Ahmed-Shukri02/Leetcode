class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        length = len(prices)
        mem = {}
        
        def dfs(i, hold):
            if i >= length:
                return 0
            if (i, hold) not in mem:
                buy, sell, h = 0, 0, 0
                if hold != None:
                    sell = prices[i] - hold + dfs(i+2, None)
                else:
                    buy = dfs(i + 1, prices[i])
                h = dfs(i + 1, hold)
                
                mem[(i, hold)] = max(buy, sell, h)
            
            return mem[(i, hold)]
        
        return dfs(0, None)