class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # Complexities
        # Time: O(n)
        # Space: O(n)
        
        
        # compute length: O(n) time with O(1) space
        length = len(nums)
        
        # compute prefix and suffix products: O(n) time and space
        pre, suff = [None for i in range(length)], [None for i in range(length)]
        for i in range(length):
            if i == 0:
                pre[0] = nums[i]
            else:
                pre[i] = nums[i] * pre[i-1]
        
        for i in range(length-1, -1, -1):
            if i == length - 1:
                suff[i] = nums[i]
            else:
                suff[i] = nums[i] * suff[i+1]
        
        final = [None for i in range(length)]
        for i in range(length):

            if i == 0:
                final[i] = suff[i+1]
            elif i == (length - 1):
                final[i] = pre[i-1]
            else:
                final[i] = pre[i-1] * suff[i+1]
        
        return final