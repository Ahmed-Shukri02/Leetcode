class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        piles = [-i for i in piles]
        # create heap from piles
        heapq.heapify(piles)
        
        # pop from top (max), half it and add it to heap k times
        for i in range(k):
            val = heapq.heappop(piles)
            heapq.heappush(piles, (val // 2))

        return -sum(piles)
        
            
            
        