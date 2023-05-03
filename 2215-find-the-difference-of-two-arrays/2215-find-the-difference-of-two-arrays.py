class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)
        f = [[], []]
        for num in s1:
            if num not in s2: f[0].append(num)
        for num in s2:
            if num not in s1: f[1].append(num)
        return f