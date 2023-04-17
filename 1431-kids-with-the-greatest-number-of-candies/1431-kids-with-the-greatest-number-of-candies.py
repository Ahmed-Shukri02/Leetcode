class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        f = []
        for n in candies:
            if n + extraCandies >= m:
                f.append(True)
            else:
                f.append(False)
        return f