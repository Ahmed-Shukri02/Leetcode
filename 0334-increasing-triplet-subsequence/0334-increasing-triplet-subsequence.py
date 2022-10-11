class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        f = s = float("inf")
        for i in nums:
            if i <= f:
                f = i
            elif i <= s:
                s = i
            else:
                return True
        return False
                
    
        