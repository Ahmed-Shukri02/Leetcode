class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        counter = 1
        while n - counter >= 0:
            n -= counter
            counter += 1

        
        return counter - 1
            