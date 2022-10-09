class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # check if both s can be mapped to t and if t can be mapped to s
        l1, l2 = len(s), len(t)
        if l1 != l2:
            return False
        
        h1, h2 = {}, {}
        for i in range(l1):
            if s[i] not in h1:
                h1[s[i]] = t[i]
            elif h1[s[i]] != t[i]:
                return False
        for i in range(l2):
            if t[i] not in h2:
                h2[t[i]] = s[i]
            elif h2[t[i]] != s[i]:
                return False
        
        return True
            
        