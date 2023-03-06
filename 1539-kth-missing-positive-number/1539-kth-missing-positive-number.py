class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        curr = 1
        for num in arr:
            while num != curr and k > 0:
                k -= 1
                curr += 1
            if k == 0:
                return curr - 1
            curr += 1
        
        return arr[-1] + k