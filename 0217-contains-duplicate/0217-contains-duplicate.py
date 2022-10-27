class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hset = set()
        for num in nums:
            if num in hset:
                return True
            hset.add(num)
        return False