class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # create hash map of letter occurances:
        hmap = {}
        for char in tasks:
            hmap[char] = hmap.get(char, 0) + 1
        
        # create max heap from occurances
        occurances = [-i for i in hmap.values()]
        heapq.heapify(occurances)
        
        # create queue for waiting to be put back into the heap
        queue = deque([])
        
        units = 0
        while occurances or queue:
    
            # check if front of queue is ready to be put back into heap
            if queue and queue[0][1] == units:
                heapq.heappush(occurances, -queue[0][0])
                queue.popleft()
                
            if not occurances: # queue is not empty but heap is, so be idle
                units += 1
                continue
                
            num = -heapq.heappop(occurances)
            num -= 1
            
            if num == 0: # do not add to queue, finished
                units += 1
                continue
            
            # add to queue with new time 
            queue.append((num, units + n + 1))
            units += 1
        
        return units