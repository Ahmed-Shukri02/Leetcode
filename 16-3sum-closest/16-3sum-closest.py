class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        length = len(nums)
        
        if length == 3:
            return sum(nums)
        
        
        minDistance = 10**4
        final = -1
        
        for i in range(0, length - 2):
            l, r = i + 1, length - 1
            remainder = target - nums[i]
            while l < r:
                twosum = nums[l] + nums[r]
                if minDistance > abs(remainder - twosum):
                    final = twosum + nums[i]
                    minDistance = abs(remainder - twosum)
                    
                if twosum == remainder:
                    return target
                elif twosum < remainder:
                    l += 1
                else:
                    r -= 1
        
        return final
        
        
        