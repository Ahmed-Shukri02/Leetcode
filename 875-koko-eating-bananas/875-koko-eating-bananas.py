import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
    
        
        min_k = max(piles)
        # do binary search
        l, r = 1, max(piles)
        while l <= r:
            mid = (l + r)//2
            # with piles[mid], see if hours is lower
            hours = 0
            for pile in piles:
                hours += ((pile - 1) // mid) + 1
            if hours <= h:
                min_k = mid
                # binary search on left side
                r = mid - 1
                continue
            else:
                # binary search on right side
                l = mid + 1
                continue
                
        return min_k
                