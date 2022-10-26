class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        length = len(nums)
        hmap = {0: 0}
        
        if length == 1:
            return False
        
        numsum = 0
        for i in range(length):
            numsum += nums[i]
            if numsum % k not in hmap:
                hmap[numsum % k] = i + 1
            elif i > hmap[numsum % k]:
                return True
        return False