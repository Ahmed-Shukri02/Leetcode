class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        
        mem = [None] * len(cost)
        length = len(cost)
        
        
        def dfs(i):
            if i >= length:
                return 0
            if mem[i]:
                return mem[i]
            
            # choose to do either one step or two steps
            one, two = dfs(i + 1), dfs(i + 2)
            mem[i] = cost[i] + min(one, two)
            return cost[i] + min(one, two)
        
        dfs(0)
        return min(mem[0], mem[1])