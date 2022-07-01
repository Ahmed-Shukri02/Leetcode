class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # Complexities:
        # Time: O(m+n)
        # Space: O(m+n)
        
        length = len(s)
        if length != len(t):
            return False
        
        # go through all letters in s and t and put it into hash map
        smap, tmap = {}, {}
        for i in range(length):
            smap[s[i]] = smap.get(s[i], 0) + 1
            tmap[t[i]] = tmap.get(t[i], 0) + 1
            
        # seach t and check if there is sufficient of the character in s
        for char in t:
            if tmap[char] > smap.get(char, 0):
                return False
        
        return True