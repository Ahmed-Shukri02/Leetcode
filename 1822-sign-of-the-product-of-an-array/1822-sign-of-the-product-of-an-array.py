class Solution:
    def arraySign(self, nums: List[int]) -> int:
        positive = True
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                positive = not positive
        return 1 if positive else -1