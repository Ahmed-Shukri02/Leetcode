class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        f, base = 0, 0
        for num in nums:
            if num != 0:
                f += math.comb(base, 2) + base
                base = 0
            else: base += 1
        
        f += math.comb(base, 2) + base
        return f