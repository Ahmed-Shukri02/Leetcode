class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n) time
        hmap = {}
        for val in nums:
            hmap[val] = hmap.get(val, 0) + 1
        
        maxSeq = 0
        for val in nums:
            # check if val is first in sequence
            if val - 1 in hmap:
                continue
            else:
                counter = 1
                while val + 1 in hmap:
                    val += 1
                    counter += 1
                if counter > maxSeq:
                    maxSeq = counter
        return maxSeq