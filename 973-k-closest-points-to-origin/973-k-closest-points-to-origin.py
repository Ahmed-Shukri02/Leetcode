class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        def euclidian(x, y):
            return (x**2 + y**2)**0.5
        
        heap = [[euclidian(i[0],i[1]), i] for i in points]        
        
        # place into max heap
        heapq.heapify(heap)
        print(heap)
        final = []
        # pop k times, and append hmap val to final
        for i in range(k):
            minVal = heapq.heappop(heap)
            
            final.append(minVal[1])
        
        return final