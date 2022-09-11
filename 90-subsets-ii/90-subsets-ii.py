class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        final = []
        curr = []
        length = len(nums)
        nums = sorted(nums)
        def helper(index,):
            # boundary functin
            if index >= length:
                # add to final
                final.append([i for i in curr])
                return
            
            # decide to include current index
            curr.append(nums[index])
            helper(index + 1)
            
            # decide not to include current index, and blacklist the number
            curr.pop()
            while index + 1 < length and nums[index] == nums[index + 1]:
                    index += 1
            helper(index + 1)
        
        helper(0)
        return final