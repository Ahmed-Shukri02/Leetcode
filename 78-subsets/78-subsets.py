class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        final = []
        curr = []
        def helper(index):
            if index >= len(nums): # out of bounds:
                final.append([i for i in curr])
                return
            
            # include index
            curr.append(nums[index])
            helper(index + 1)
            
            # not include index
            curr.pop()
            helper(index + 1)
        
        helper(0)
        return final