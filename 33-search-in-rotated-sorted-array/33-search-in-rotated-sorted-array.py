class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # start by finding pivot of rotated array
        # binary search for element where nums[i+1] < nums[i]
        # if nums[i + 1] >= nums[i]:
        #   if nums[i] >= nums[l] it means that we have not reached pivot yet (left side of pivot): eliminate left side
        #   if nums[i] < nums[l] it means that we have passed pivot (right side): eliminate right side
        
        length = len(nums)
        l, r = 0, length -1

        pivot = None
        while l <= r:
            i = (l + r)//2
            if i == length - 1:
                break   
            elif nums[i + 1] >= nums[i]:
                if nums[i] >= nums[l]:
                    # elimate left side
                    l = i + 1
                    continue
                else:
                    # elimate right side
                    r = i - 1
                    continue
            else:
                pivot = i
                break

        if pivot == None:
            # do regular binary search for target
            return self.binary(nums, target, 0, length - 1)


        else:
            # array is rotated, do rotated binary search
            # if target > nums[0], binray search on left side of pivot. else binary search on right side of pivot
            if target == nums[0]:
                return 0
            elif target > nums[0]:
                return self.binary(nums, target, 0, pivot)
            else:
                return self.binary(nums, target, pivot + 1, length - 1)

    
    
    def binary(self, nums, target, l, r):
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                # eliminate right side
                r = mid - 1
                continue
            elif nums[mid] < target:
                # eliminate left side
                l = mid + 1
                continue
            else:
                return mid
        return -1 
        
                