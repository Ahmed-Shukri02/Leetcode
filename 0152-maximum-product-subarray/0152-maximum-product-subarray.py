class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        length = len(nums)
        mem = [[1, 1]] * length # 0 = max, 1 = min
        mem[-1] = [nums[-1]] * 2
        for i in range(length - 2, -1, -1):
            p = (nums[i], nums[i] * mem[i + 1][0], nums[i] * mem[i + 1][1]) # number on its own, num * max possible subarr prod, num * min possible subarr prod
            mem[i] = [max(p), min(p)]
        
        return max(mem)[0]