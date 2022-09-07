class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        # heapify array

        for i in range(len(stones)):
            stones[i] = -stones[i]
            
        heapq.heapify(stones)
        
        while len(stones) > 1:
            rock1, rock2 = heapq.heappop(stones), heapq.heappop(stones)
            if rock1 == rock2:
                continue
            
            heapq.heappush(stones, -abs(rock1 - rock2))
        
        print stones
        if stones:
            return -stones[0]
        return 0