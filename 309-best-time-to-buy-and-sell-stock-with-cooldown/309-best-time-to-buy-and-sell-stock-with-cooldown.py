class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        length = len(prices)
        mem = [[None for i in range(length)] for i in range(2)] # 0: holding, 1: not holding


        def dfs(i, hold):
            if i > length - 1:
                return 0
            
            if hold:
                if mem[0][i] != None:
                    return mem[0][i]

                # make two choices, sell and do cooldown or hold
                sell = prices[i] + dfs(i + 2, not hold)
                holdC = dfs(i + 1, hold)
                mem[0][i] = max(sell, holdC)
                return mem[0][i]
            else:
                if mem[1][i] != None:
                    return mem[1][i]

                # make two choices, buy or continue with nothing
                buy = dfs(i + 1, not hold) - prices[i]
                con = dfs(i + 1, hold)
                mem[1][i] = max(buy, con)
                return mem[1][i]

        return dfs(0, [])