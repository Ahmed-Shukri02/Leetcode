class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # Complexities: 
        # Time: O(n)
        # Space: O(1)
        
        # find length: O(n) time complexity
        length = len(numbers)
        
        # set pointers to the beginning and end
        p1, p2 = 0, length - 1
        while p2 > p1:
            val = numbers[p1] + numbers[p2]
            if val > target:
                p2 -= 1
            elif val < target:
                p1 += 1
            else: return [p1 + 1, p2 + 1]
        
        return -1