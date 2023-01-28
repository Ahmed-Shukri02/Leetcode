class SummaryRanges:

    def __init__(self):
        # heap
        self.interval = []

    def addNum(self, value: int) -> None:
        if not self.interval:
            self.interval = [[value, value]]
            return
        tmp = self.interval
        f = []
        curr_interval = [value, value]
        for i in range(len(tmp)):
            if curr_interval[0] > tmp[i][1] + 1:
                f.append(tmp[i])
                continue
            elif curr_interval[1] + 1 < tmp[i][0]:
                f.append(curr_interval)
                f += tmp[i:]
                self.interval = f
                return 
            curr_interval = [min(curr_interval[0], tmp[i][0]), max(curr_interval[1], tmp[i][1])]
        f.append(curr_interval)
        self.interval = f

    def getIntervals(self) -> List[List[int]]:
        return self.interval


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()