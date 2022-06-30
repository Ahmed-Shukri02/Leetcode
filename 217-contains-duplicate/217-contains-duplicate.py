class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # O(n) time, O(n) space
        
        hmap = {}
        for val in nums:
            if val not in hmap:
                hmap[val] = 1
            else:
                hmap[val] += 1
        
        for val in nums:
            if hmap[val] > 1:
                return True
        return False