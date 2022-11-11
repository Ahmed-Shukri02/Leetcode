class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        prev = nums[0]
        i = 1
        while i < length:
            if nums[i] == prev:
                nums.pop(i)
                length -= 1
                continue
            prev = nums[i]
            i += 1
        
        return len(nums)