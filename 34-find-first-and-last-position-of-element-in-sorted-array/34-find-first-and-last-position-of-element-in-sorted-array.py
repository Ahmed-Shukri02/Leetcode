class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # Complexities
        # Time: O(logn)
        # Space: O(1)
        
        
        length = len(nums)
        final = [-1, -1]
        # do binary search from left target
        l, r = 0, length -1
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                if mid > 0 and nums[mid] == nums[mid - 1]:
                    r = mid - 1
                else:
                    final[0] = mid
                    break
               
        # do binary search for right target
        l, r = 0, length -1
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                if mid < length -1 and nums[mid] == nums[mid + 1]:
                    l = mid + 1
                else:
                    final[1] = mid
                    break
        
        
        return final
            
                
            
        