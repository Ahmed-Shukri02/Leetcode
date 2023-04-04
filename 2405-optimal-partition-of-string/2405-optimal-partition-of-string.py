class Solution:
    def partitionString(self, s: str) -> int:
        f = 1
        hset = set()
        for char in s:
            if char in hset:
                f += 1
                hset = set()
            hset.add(char)
        
        return f