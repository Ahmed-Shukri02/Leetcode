# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n
        while l <= r:
            mid = (l + r)//2
            if isBadVersion(mid) and isBadVersion(mid - 1): # everything after it is bad, so remove it
                r = mid - 1
            elif not isBadVersion(mid): # everything before it is good, so remove it
                l = mid + 1
            else: # current version is bad and previous version is good: we found the first bad version
                return mid
        
                