class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        n = len(tasks)
        # sort by enqueue time
        tasks = sorted([(tasks[i][0], tasks[i][1], i) for i in range(n)], key = lambda x: x[0])
        i, t = 0, 0
        final, h = [], []
        while i < n:
            while i < n and t >= tasks[i][0]:
                # add current to heap
                heapq.heappush(h, (tasks[i][1], tasks[i][2]))
                i += 1
            if h:
                processTime, index = heapq.heappop(h)
                final.append(index)
                t += processTime
            elif i < n: # idle
                t = tasks[i][0]
        
        # add all remainding processes
        while h:
            final.append(heapq.heappop(h)[1])
        return final
                