class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        hset = set()
        dup = None
        for num in nums:
            if num in hset:
                dup = num
            hset.add(num)
        
        for i in range(1, len(nums) + 1):
            if i not in hset:
                return [dup, i]
        