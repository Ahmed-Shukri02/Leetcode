class SmallestInfiniteSet:

    def __init__(self):
        self.h = []
        self.curr = 1
        self.s = set()

    def popSmallest(self) -> int:
        if not self.h:
            self.curr += 1
            return self.curr - 1
        self.s.remove(self.h[0])
        return heapq.heappop(self.h)


    def addBack(self, num: int) -> None:
        if num < self.curr and num not in self.s:
            heapq.heappush(self.h, num)
            self.s.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)