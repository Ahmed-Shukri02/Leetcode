class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        
        # find pivot: i where nums[i + 1] < nums[i]
        l, r = 0, length - 1
        while l <= r:
            mid = (l + r) // 2
            if mid == length - 1:
                break
            if nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            elif nums[mid] < nums[0]: # we're on right side of pivot
                r = mid - 1
            else:
                l = mid + 1
        # no pivot
        return nums[0]
            