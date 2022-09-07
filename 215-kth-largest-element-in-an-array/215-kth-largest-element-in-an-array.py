class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = [-i for i in nums] # O(n)
        heapq.heapify(nums) # O(n)
        
        while k > 0:
            val = heapq.heappop(nums)
            k -= 1
        return -val
            