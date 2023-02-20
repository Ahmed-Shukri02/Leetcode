class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # search for target

        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)

        while l <= r:
            mid = (r+l)//2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
            
        if target > nums[l]: l += 1
        return l
