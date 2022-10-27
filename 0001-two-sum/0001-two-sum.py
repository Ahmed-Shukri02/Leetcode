class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hmap = {}
        length = len(nums)
        for i in range(length):
            if nums[i] in hmap:
                return [i, hmap[nums[i]]]
            hmap[target - nums[i]] = i