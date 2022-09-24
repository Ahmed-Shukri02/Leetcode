class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        mem = {}
        
        def dfs(numsum):
            if numsum == amount:
                return 1
            elif numsum > amount:
                return None
            
            if numsum in mem:
                return mem[numsum]
            
            new = []
            for coin in coins:
                res = dfs(numsum + coin)
                if res:
                    new.append(1 + res)
                    
            minCoins = min(new) if new else None
            mem[numsum] = minCoins
            return minCoins
        
        sol = dfs(0)
        return sol - 1 if sol else -1