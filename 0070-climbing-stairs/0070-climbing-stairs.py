class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        n += 1
        return int(round(((((1+(5**0.5))/2)**n)-(((1-(5**0.5))/2)**n))/(5**0.5)))