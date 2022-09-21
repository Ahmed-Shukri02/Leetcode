class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        final = []
        length = len(nums)
        mem = [None] * length
        
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        elif length == 2:
            return max(nums[0], nums[1])
        
        def dfs(i):
            if i >= length:
                return 0
            if mem[i] != None:
                return mem[i]
            
            # max profit you can get from robbing or skipping
            rob, skip = dfs(i + 2) + nums[i], dfs(i + 1)
            mem[i] = max(rob, skip)
            return max(rob, skip)
        
        return dfs(0)