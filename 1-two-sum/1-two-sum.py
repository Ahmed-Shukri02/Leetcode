class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # method 1: O(n^2) attempt
        
        # Complexities:
        # Time: O(n^2)
        # Space: O(1)
        
        
        # equation a + b = target
        
        # first find length of array: time complexity O(n)
        length = len(nums)
        
        for i in range(length):
            b = target - nums[i]
            # linear search for b
            
            # if a and b are the same
            if b == nums[i]:
                for j in range(i+1, length):
                    if nums[j] == b: return [i, j]
            
            # if they arent
            else:
                for j in range(length):
                    if nums[j] == b: return [i, j]
        
        
        return -1
    
    
        # method 2: O(nlogn) attempt
        
        
        # Complexities:
        # Time: O(nlogn)
        # Space: O(n)
        
        # first find length of array: time complexity O(n)
        length = len(nums)
        
        # sort array: time complexity O(nlogn)
        nums1 = sorted(nums)
        
        # for each value, do binary search for corresponding additive O(n * log(n))
        for i in range(length):
            b = target - nums1[i]
            
            # binary search for b
            low, high = 0, length - 1
            
            while low <= high:
                mid = (high+low) // 2
                
                if nums1[mid] == b: # WILL ONLY RUN ONCE
                    
                    val1, val2 = nums1[mid], nums1[i]
                    final = []
                    if(val1 == val2):
                        for i in range(0, length):
                            if nums[i] == val1:
                                final.append(i)
                                break
                        for j in range(final[0] + 1, length):
                            if nums[j] == val2:
                                final.append(j)
                    else:
                        for i in range(length):
                            if nums[i] == val1:
                                final.append(i)
                        for j in range(length):
                            if nums[j] == val2:
                                final.append(j)
        
                    return final
        
        
                elif nums1[mid] > target:
                    high = mid - 1
                
                elif nums1[mid] < target:
                    low = mid + 1
                    
