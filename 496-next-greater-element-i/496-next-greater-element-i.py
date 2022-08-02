class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        stack = []
        hmap = {}
        length = len(nums2)
        
        r = length - 1
        while r >= 0:
            hmap[nums2[r]] = -1
            
            if not stack:
                stack.append(nums2[r])
                r -= 1
                continue
            
            while stack and nums2[r] > stack[-1]:
                stack.pop()
            
            if stack:
                hmap[nums2[r]] = stack[-1]
            
            stack.append(nums2[r])
            r -= 1
        
        final = []
        for val in nums1:
            final.append(hmap[val])
        
        return final