class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        f = 0
        for i in range(len(nums)):
            l, r = 0, len(nums) - 1
            # bin search where nums[i] + n <= target
            t = target - nums[i]
            while l <= r:
                m = (l + r) // 2
                if nums[m] <= t:
                    l = m + 1
                else:
                    r = m - 1
            if l - i - 1 >= 0: f += (2 ** (l - i - 1))

        return f % (10**9 + 7)
        
