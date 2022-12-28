class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        final = []
        def helper(arr, curr):
            if not arr:
                final.append([i for i in curr])
                return
            for num in arr:
                tmp = [i for i in arr]
                curr.append(num)
                tmp.remove(num)
                helper(tmp, curr)
                curr.pop()
        helper(nums, [])
        return final

    ### update text
            