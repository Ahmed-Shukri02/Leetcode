class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # Complexities:
        # Time: O(n^2)
        # Space: O(n)? maybe?
        
        # find length and sort: O(n) and O(nlogn)
        length = len(nums)
        nums = sorted(nums)
        
        
        # 3 pointer method: O(n^2)
        final = []
        for i in range(length):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            target = - nums[i] # (0 - num) is b + c
            p2, p3 = i + 1, length - 1 
            
            # do twosum for target
            while p2 < p3:
                val = nums[p2] + nums[p3]
                if val < target:
                    p2 += 1
                elif val > target:
                    p3 -= 1
                else:
                    final.append([nums[i], nums[p2], nums[p3]])
                    p2 += 1
                    while nums[p2] == nums[p2-1] and p2 < p3:
                        p2 += 1

                
            
        return final
        