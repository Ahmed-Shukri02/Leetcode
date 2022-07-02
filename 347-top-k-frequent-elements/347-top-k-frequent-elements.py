class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # find length of nums: O(n) time
        length = len(nums)
        
        
        # O(n) time and space
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1
        
        # O(n) space
        sort = [[] for i in range(length + 1)]
        
        for key in hmap.keys():
            sort[hmap[key]].append(key)
        
        final = []
        for i in range(len(sort) - 1, 0, -1):
            for num in sort[i]:
                final.append(num)
                if len(final) == k: return final