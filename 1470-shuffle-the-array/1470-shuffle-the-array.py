class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        f = []
        for i in range(n):
            f.append(nums[i])
            f.append(nums[n + i])
        return f