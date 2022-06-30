class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # O(n) time, O(n) space
        
        hmap = {}
        i = 0
        while True: # always one solution
            val = target - nums[i]
            if val in hmap:
                return [hmap[val], i]
            else:
                hmap[nums[i]] = i
            i += 1
        return -1