class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        maxArea = 0
        length = len(height)
        l, r = 0, length - 1
        while l < r:
            area = min(height[l], height[r]) * (r-l)
            
            if area > maxArea:
                maxArea = area
            
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        
        
        return maxArea