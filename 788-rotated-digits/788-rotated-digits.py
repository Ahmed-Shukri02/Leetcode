class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """

        count = 0
        for d in range(1, n+1):
            d = str(d)
            if '3' in d or '4' in d or '7' in d:
                continue
            if '2' in d or '5' in d or '6' in d or '9' in d:
                count+=1
        return count
    
    
        