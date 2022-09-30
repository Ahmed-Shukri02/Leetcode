class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        length = len(nums)
        mem = [0 for i in range(length)]
        mem[-1] = nums[-1]
        maxVal = mem[-1]
        
        for j in range(length - 2, -1, -1):
            mem[j] = max(nums[j], nums[j] + mem[j + 1])
            maxVal = max(maxVal, mem[j])
        
        return maxVal
        