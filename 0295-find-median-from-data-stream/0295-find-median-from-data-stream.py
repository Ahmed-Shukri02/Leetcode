class MedianFinder(object):

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # add to small: max
        heapq.heappush(self.small, -num)
        
        # check if largest value in small is larger than smallest value in large. If so, swap
        if self.small and self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # check if inequality is higher than 1, if so, add to min heap
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # check if inequality is higher than 1, if so, add to max heap
        if len(self.large) > len(self.small) + 1:
            val = -heapq.heappop(self.large)
            heapq.heappush(self.small, val)
        
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            if (-self.small[0] + self.large[0]) % 2 == 1:
                return ((-self.small[0] + self.large[0]) // 2) + 0.5
            else:
                return (-self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()