class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """

        depth, maxDepth = 0, 0
        for char in s:
            if char == ")":
                depth -=1
            elif char == "(":
                depth += 1
            
            maxDepth = max(depth, maxDepth)     
        
        return maxDepth
                