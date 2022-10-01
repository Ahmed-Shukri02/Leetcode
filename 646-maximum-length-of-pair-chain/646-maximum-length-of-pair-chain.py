class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if not pairs:
            return 0
        
        pairs = sorted(pairs, key= lambda x: x[1])
        
        length = len(pairs)
        mem = [1] * length
        final = 1
        
        # mem[-1] = 1 ==> base case.
        for i in range(length -2, -1, -1):
            maxC = 1
            for j in range(i + 1, length):
                if pairs[i][1] < pairs[j][0]:
                    maxC = max(maxC, 1 + mem[j])
            mem[i] = maxC
            
            final = max(final, maxC)
        
        return final