class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        mem = [0] * length
        mem[length - 1] = 1

        for i in range(length - 2, -1, -1):
            for j in range(i + 1, min(length, i + nums[i] + 1)):
                if mem[j]: 
                    mem[i] = 1
                    break
        return mem[0] == 1
