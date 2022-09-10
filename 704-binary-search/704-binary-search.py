class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l, r = 0, len(nums) - 1
        while l<=r:
            mid = (l+r)//2
            if target > nums[mid]: # remove left side
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1
                