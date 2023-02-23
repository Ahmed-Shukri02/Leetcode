class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # zip profits and capital together
        arr = sorted([(capital[i], profits[i]) for i in range(len(profits))]) # sort profits from largest to smallest and capital from smallest to largest
        h = []
        f, p = w, 0

        for i in range(k):
            while p < len(arr) and arr[p][0] <= f:
                heapq.heappush(h, -arr[p][1])
                p += 1
            
            if not h:
                break

            f -= heapq.heappop(h)


        return f

            
            
            
            

            

            
            

