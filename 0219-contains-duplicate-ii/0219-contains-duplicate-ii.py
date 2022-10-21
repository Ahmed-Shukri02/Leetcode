class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        hmap = {}
        for i in range(len(nums)):
            if nums[i] in hmap and abs(i - hmap[nums[i]]) <= k:
                return True
            hmap[nums[i]] = i
        return False