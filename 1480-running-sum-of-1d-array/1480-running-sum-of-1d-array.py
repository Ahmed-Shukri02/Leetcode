class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #edge case
        if not nums:
            return nums
    
        prefSum = [nums[0]]
        for i in range(1, len(nums)):
            prefSum.append(prefSum[i - 1] + nums[i])
        
        return prefSum