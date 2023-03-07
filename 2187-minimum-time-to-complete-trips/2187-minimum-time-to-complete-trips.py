class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def TT(steps):
            return sum([steps // i for i in time])
        
        max_b = min(time) * totalTrips
        l, r = 1, max_b
        # find a time t such that TT(t - 1) < totalTrips but TT(t) >= totalTrips
        while l <= r:
            mid = (l + r) // 2
            if TT(mid) < totalTrips:
                l = mid + 1
            elif TT(mid) >= totalTrips:
                r = mid - 1
        return l
