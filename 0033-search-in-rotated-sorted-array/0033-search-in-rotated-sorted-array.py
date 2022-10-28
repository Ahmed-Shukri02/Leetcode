class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find pivot
        length = len(nums)
        l, r = 0, length - 1
        
        pivot = None
        
        while l <= r:
            i = (l + r) // 2
            if i == length - 1:
                break
            
            if nums[i + 1] < nums[i]:
                pivot = i
                break
            elif nums[i] < nums[0]:
                r = i - 1
            else:
                l = i + 1
        
        if pivot == None:
            l, r = 0, length - 1
        elif target == nums[0]:
            return 0
        elif target > nums[0]: # should be on 
            l, r = 0, pivot
        else:
            l, r = pivot + 1, length - 1
        
        while l <= r:
            i = (l + r) // 2
            if nums[i] == target:
                return i
            elif nums[i] > target:
                r = i - 1
            else:
                l = i + 1
        return -1