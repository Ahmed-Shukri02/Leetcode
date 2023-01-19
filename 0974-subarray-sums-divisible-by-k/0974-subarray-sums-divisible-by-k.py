class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        
        f = 0
        hmap = defaultdict(int)
        for pre in prefix:
            takeaway = pre % k
            f += hmap[takeaway]
            hmap[takeaway] += 1
        print(hmap)
        return f