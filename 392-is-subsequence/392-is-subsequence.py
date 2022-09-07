class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l, p = 0, 0
        # traverse t, if s[l] = t[p], then l += 1.
        length = len(s)
        while l < length and p < len(t):
            if s[l] == t[p]:
                l += 1
                if l >= length:
                    break
            p += 1
        
        return l == length