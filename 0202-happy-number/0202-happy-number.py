class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hset = set()
        s = str(n)
        
        while s != "1":
            if s in hset:
                return False
            hset.add(s)
            ns = 0
            for char in s:
                ns += int(char) ** 2 
            s = str(ns)
        return True