class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # sort nums
        nums.sort()
        
        length = len(nums)
        # single pointer that goes through array
        final = []
        slow = 0
        for slow in range(length):
            if slow > 0 and nums[slow] == nums[slow-1]:
                continue
            
            target =  0 - nums[slow]
            # target is target for twosum search from i+1 to length -1
            l, r = slow+1, length - 1
            while r > l:
                sol = nums[r] + nums[l]
                if sol > target:
                    r -= 1
                elif sol < target:
                    l += 1
                else:
                    final.append([nums[slow], nums[r], nums[l]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return final