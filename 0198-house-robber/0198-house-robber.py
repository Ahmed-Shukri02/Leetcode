class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        mem = [(0, 0)] * length # (max with, max without)
        mem[length-1] = (nums[length-1], 0)
        
        for i in range(length - 2, -1, -1):
            mem[i] = (nums[i] + mem[i+1][1], max(mem[i+1]))
        
        return max(mem[0])
            