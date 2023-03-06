class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            ml = arr[mid] - mid - 1
            if ml >= k:
                r = mid - 1
            else:
                l = mid + 1
        return l + k
