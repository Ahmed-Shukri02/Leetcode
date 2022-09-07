class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        length1, length2 = len(s), len(t)
        if length1 != length2:
            return False
        hmap = {}
        for i in range(length1):
            if s[i] in hmap:
                del hmap[s[i]]
            hmap[s[i]] = t[i]
                
        for i in range(length1):
            if hmap[s[i]] != t[i]:
                return False
            
        hmap2 = {}
        for i in range(length1):
            if t[i] in hmap2:
                del hmap2[t[i]]
            hmap2[t[i]] = s[i]
                
        for i in range(length1):
            if hmap2[t[i]] != s[i]:
                return False
        
        return True
        