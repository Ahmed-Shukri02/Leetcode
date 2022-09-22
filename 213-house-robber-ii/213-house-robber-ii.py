class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def dfs(i, arr):
            if i >= len(arr):
                return 0
            if mem[i] != None:
                return mem[i]
            
            rob, skip = arr[i] + dfs(i + 2, arr), dfs(i + 1, arr)
            mem[i] = max(rob, skip)
            return max(rob, skip)
        
        length = len(nums)
        
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        elif length == 2:
            return max(nums)
        
        mem = [None] * length
        one = dfs(0, nums[0:-1])
        mem = [None] * length
        two = dfs(0, nums[1:])
        
        return max(one, two)