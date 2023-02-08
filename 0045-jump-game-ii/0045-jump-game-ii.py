class Solution:
    def jump(self, nums: List[int]) -> int:

        mem = {}
        self.min = float("inf")
        def dfs(i, path):
            if i == len(nums) - 1:
                self.min = min(self.min, path)
                return 0
            elif i in mem:
                self.min = min(self.min, path + mem[i])
                return mem[i]

            m = float("inf")
            for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
                m = min(m, 1 + dfs(j, path + 1))
            mem[i] = m
            return m
        
        dfs(0, 0)
        return self.min
