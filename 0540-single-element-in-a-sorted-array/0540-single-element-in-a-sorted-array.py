class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        if len(nums) == 1:
            return nums[0]

        while l <= r:
            mid = (l + r)//2
            if mid == 0:
                if nums[1] != nums[0]:
                    return nums[0]
                l += 1
                continue
            elif mid == len(nums) - 1:
                return nums[-1]

            if nums[mid - 1] != nums[mid] and nums[mid + 1] != nums[mid]:
                return nums[mid]
            elif nums[mid - 1] == nums[mid]:
                if mid % 2 == 0: # consider left
                    r = mid - 1
                else: # consider right
                    l = mid + 1
            else:
                if (len(nums) - mid - 1) % 2 == 0: # consider right
                    l = mid + 1
                else: # consider left
                    r = mid - 1
        
        return -1