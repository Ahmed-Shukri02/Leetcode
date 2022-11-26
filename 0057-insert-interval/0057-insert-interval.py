class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        final = []
        length = len(intervals)
        
        for i in range(length):
            if newInterval[0] > intervals[i][1]:
                final.append(intervals[i])
                continue
            elif newInterval[1] < intervals[i][0]:
                final.append(newInterval)
                return final + intervals[i:]
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        final.append(newInterval)
        return final

        