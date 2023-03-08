class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def time(k):
            return sum([ceil(i / k) for i in piles])
        
        l, r = 1, sum(piles)
        while l <= r:
            # find rate such that time(k - 1) < h and time(k) >= h
            mid = (l + r) // 2
            if time(mid) > h:
                l = mid + 1
            else:
                r = mid - 1
        return l