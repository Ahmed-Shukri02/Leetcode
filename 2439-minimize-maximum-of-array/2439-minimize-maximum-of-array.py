class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        pref_sum = 0
        f = 0
        for i in range(len(nums)):
            pref_sum += nums[i]
            f = max(f, ceil(pref_sum / (i + 1)))
        return f
