class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(w):
            p, curr = 1, 0
            for weight in weights:
                if curr + weight > w:
                    p, curr = p + 1, 0
                curr += weight

            return p <= days
        
        l, r = max(weights), sum(weights)
        while l <= r:
            mid = (l + r) // 2
            if feasible(mid):
                r = mid - 1
            else:
                l = mid + 1

        return l
