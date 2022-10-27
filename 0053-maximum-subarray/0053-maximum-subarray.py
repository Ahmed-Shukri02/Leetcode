class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        mem = [0 for i in range(length)]
        mem[-1] = nums[-1]
        
        for i in range(length - 2, -1, -1):
            mem[i] = max(nums[i], nums[i] + mem[i + 1])
        
        return max(mem)