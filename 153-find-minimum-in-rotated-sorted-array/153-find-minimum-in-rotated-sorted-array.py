class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # find pivot index i. minimum is nums[i+1] (where pivot is defined as last element before rotation)
        length = len(nums)
        l, r = 0, length - 1
        while l <= r:
            i = (l + r)//2
            
            # guard clause: l and r converged to last element. No net rotation achieved
            if i == length - 1:
                break
            
            # guard clause: pivot found
            if nums[i + 1] < nums [i]:
                return nums[i + 1]
            
            # cannot be equal since unique, so only other case is nums[i+1] > nums[i]
            if nums[i] >= nums[0]:
                # pivot right to i, remove left
                l = i + 1
                continue
            else:
                # pivot left to i, remove right
                r = i - 1
                continue
        
        # if nothing has been returned, then no net rotation achieved. return minimum (in this case first element)
        return nums[0]