class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # use two pointer method
        length = len(numbers)
        
        l, r = 0, length - 1
        while r > l:
            sol = numbers[l] + numbers[r]
            if sol > target:
                r -= 1
                continue
            elif sol < target:
                l += 1
            else:
                return [l + 1, r + 1]