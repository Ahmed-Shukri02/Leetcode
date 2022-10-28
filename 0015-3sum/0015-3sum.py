class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O (n^2)
        # do 2sum for every elem
        length = len(nums)
        nums = sorted(nums)
        
        tr = set()
        for i in range(length):
            remainder = 0 - nums[i]
            # do 2sum with remainder
            hset = set()
            for j in range(i + 1, length):
                if (remainder - nums[j]) in hset:
                    ans = (nums[i], nums[j], remainder - nums[j])
                    if ans not in tr: tr.add(ans)
                hset.add(nums[j])
            
        return list(tr)