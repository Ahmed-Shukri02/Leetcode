class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        arr = [-(i * 2) if i % 2 else -i for i in set(nums)]
        min_val = -max(arr)
        f = float("inf")

        heapq.heapify(arr)
        while arr[0] % 2 == 0:
            val = -heapq.heappop(arr)
            f = min(f, val - min_val)
            min_val = min(min_val, val // 2)
            heapq.heappush(arr, -val // 2)
        return min(f, -arr[0] - min_val)


