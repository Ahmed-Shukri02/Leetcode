class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        # dp with complexity o(nr) where r is additional rocks
        
        mem = {}
        length = len(rocks)
        for i in range(length):
            capacity[i] = capacity[i] - rocks[i]
        capacity = sorted(capacity)
        f = 0
        for i in range(length):
            remainder = additionalRocks - capacity[i]
            if remainder < 0:
                break
            additionalRocks = remainder
            f += 1
        return f
        