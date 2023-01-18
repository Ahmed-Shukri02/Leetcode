class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSub, minSub = [float("-inf")] * len(nums), [float("inf")] * len(nums)
        maxSub[0] = minSub[0] = nums[0]
        for i in range(1, len(nums)):
            maxSub[i], minSub[i] = max(nums[i], nums[i] + maxSub[i - 1]), min(nums[i], nums[i] + minSub[i - 1])
        maxVal, minVal = max(maxSub), min(minSub)
        if sum(nums) - minVal == 0:
            # entire array is negative, return max of subarry
            return maxVal
        return max(maxVal, sum(nums) - minVal)
            