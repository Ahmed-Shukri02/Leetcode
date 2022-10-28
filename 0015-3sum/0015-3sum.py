class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O (n^2)
        # do 2sum for every elem
        length = len(nums)
        nums = sorted(nums)
        
        tr = []
        for i in range(length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            remainder = 0 - nums[i]
            # do 2sum with remainder
            l, r = i + 1, length - 1
            while l < r:
                numsum = nums[l] + nums[r]
                if numsum > remainder:
                    r -= 1
                elif numsum < remainder:
                    l += 1
                else:
                    tr.append([nums[r], nums[l], nums[i]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return tr