class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # create prefix sum
        preSums = [nums[0]]
        length = len(nums)
        total = sum(nums)
        # edge case: for first elem
        if total == nums[0]:
            return 0
        
        for i in range(1, length):
            prefix = preSums[i - 1] + nums[i]
            postfix = total - preSums[i - 1]
            if prefix == postfix:
                return i
            preSums.append(preSums[i - 1] + nums[i])
        return -1
        
        
            